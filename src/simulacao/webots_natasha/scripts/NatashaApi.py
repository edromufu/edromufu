#!/usr/bin/env python3

import os
import sys
import math
import re
import socket
import time

import rospy
import rospkg
import struct
import copy
from threading import Lock
from urdf_parser_py.urdf import URDF

from rosgraph_msgs.msg import Clock
from geometry_msgs.msg import PointStamped, Vector3
from sensor_msgs.msg import CameraInfo, Image, JointState
from movement_msgs.msg import *

import messages_pb2


class NatashaApi():
    def __init__(self):
        rospack = rospkg.RosPack()
        self._package_path = rospack.get_path("webots_natasha")

        rospy.init_node("edrom_robocup_api")
        rospy.loginfo("Initializing edrom_robocup_api...", logger_name="rc_api")

        self.camera_FOV = 1.04
        self.motorNames = [ 'RARM_0 [shoulder]', 'LARM_0 [shoulder]', 
                            'RARM_1', 'LARM_1',
                            'LARM_2', 'RARM_2',
                            'RLEG_0', 'LLEG_0',
                            'RLEG_1 [hip]', 'LLEG_1 [hip]',
                            'RLEG_2', 'LLEG_2',
                            'RLEG_3', 'LLEG_3',
                            'RLEG_4', 'LLEG_4', 
                            'RFOOT',  'LFOOT',
                            'HEAD_0', 'HEAD_1' ]

        # Parse URDF
        urdf_path = os.path.join(rospack.get_path('webots_natasha'), 'urdf', 'natasha.urdf')
        urdf = URDF.from_xml_file(urdf_path)
        joints = [joint for joint in urdf.joints if joint.type == 'continuous']
        #self.velocity_limits = {joint.name: joint.limit.velocity for joint in joints}
        motor_name = [joint.name for joint in joints]

        self.position_sensors = [self.joint_to_webots(name) + "_sensor" for name in motor_name]
        self.sensors_names = [
            "Camera",
            "Accelerometer"
            ]
        self.sensors_names.extend(self.position_sensors)

        self.joint_command = WebotsMsg()

        self.create_publishers()
        self.create_subscribers()

        addr = os.environ.get('ROBOCUP_SIMULATOR_ADDR')
        # we will try multiple times till we manage to get a connection
        self.socket = None
        while not rospy.is_shutdown() and self.socket is None:
            self.socket = self.get_connection(addr)
            time.sleep(1) #dont use ros time since it is maybe not available

        self.first_run = True
        self.published_camera_info = False

        self.joint_command_mutex = Lock()

        self.run()

    def receive_msg(self):
        msg_size = self.socket.recv(4)
        msg_size = struct.unpack(">L", msg_size)[0]

        data = bytearray()
        while len(data) < msg_size:
            packet = self.socket.recv(msg_size - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data

    def run(self):
        while not rospy.is_shutdown():
            # Parse sensor
            msg = self.receive_msg()
            self.handle_sensor_measurements_msg(msg)

            sensor_time_steps = None
            if self.first_run:
                sensor_time_steps = self.get_sensor_time_steps(active=True)
            self.send_actuator_requests(sensor_time_steps)
            self.first_run = False
        self.close_connection()

    def create_publishers(self):
        self.pub_clock = rospy.Publisher('/clock', Clock, queue_size=1)
        self.pub_server_time_clock = rospy.Publisher('/server_time_clock', Clock, queue_size=1)
        self.pub_camera = rospy.Publisher('camera/image_proc', Image, queue_size=1)
        self.pub_camera_info = rospy.Publisher('camera/camera_info', CameraInfo, queue_size=1, latch=True)
        self.pub_imu = rospy.Publisher('/webots_natasha/behaviour_controller', Vector3, queue_size=1)
        self.pub_joint_states = rospy.Publisher('joint_states', JointState, queue_size=1)

    def create_subscribers(self):
        self.sub_joint_command = rospy.Subscriber('opencm/conversion', WebotsMsg, self.joint_command_cb, queue_size=1)

    def joint_command_cb(self, msg):
        with self.joint_command_mutex:
            self.joint_command = msg

    def get_connection(self, addr):
        host, port = addr.split(':')
        port = int(port)
        rospy.loginfo(f"Connecting to '{addr}'", logger_name="rc_api")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((host, port))
            response = sock.recv(8).decode('utf8')
        except ConnectionRefusedError:
            rospy.logerr(f"Connection refused by '{addr}'", logger_name="rc_api")
            return None
        if response == "Welcome\0":
            rospy.loginfo(f"Successfully connected to '{addr}'", logger_name="rc_api")
            return sock
        elif response == "Refused\0":
            rospy.logerr(f"Connection refused by '{addr}'", logger_name="rc_api")
            return None
        else:
            rospy.logerr(f"Could not connect to '{addr}'\nGot response '{response}'", logger_name="rc_api")
            return None

    def close_connection(self):
        self.socket.close()

    def handle_sensor_measurements_msg(self, msg):
        s_m = messages_pb2.SensorMeasurements()
        s_m.ParseFromString(msg)

        self.handle_time(s_m.time)
        self.handle_real_time(s_m.real_time)
        self.handle_messages(s_m.messages)
        self.handle_imu_data(s_m.accelerometers)
        self.handle_camera_measurements(s_m.cameras)
        self.handle_position_sensor_measurements(s_m.position_sensors)

    def handle_time(self, time):
        # time stamp at which the measurements were performed expressed in [ms]
        secs = time / 1000
        ros_time = rospy.Time.from_seconds(secs)
        self.stamp = ros_time
        msg = Clock()
        msg.clock.secs = ros_time.secs
        msg.clock.nsecs = ros_time.nsecs
        self.pub_clock.publish(msg)

    def handle_real_time(self, time):
        # real unix time stamp at which the measurements were performed in [ms]
        msg = Clock()
        msg.clock.secs = time // 1000
        msg.clock.nsecs = (time % 1000) * 10**6
        self.pub_server_time_clock.publish(msg)

    def handle_messages(self, messages):
        for message in messages:
            text = message.text
            if message.message_type == messages_pb2.Message.ERROR_MESSAGE:
                rospy.logerr(f"RECEIVED ERROR: '{text}'", logger_name="rc_api")
            elif message.message_type == messages_pb2.Message.WARNING_MESSAGE:
                #rospy.logwarn(f"RECEIVED WARNING: '{text}'", logger_name="rc_api")
                pass
            else:
                rospy.logwarn(f"RECEIVED UNKNOWN MESSAGE: '{text}'", logger_name="rc_api")

    def handle_imu_data(self, accelerometers):
        # Body IMU
        imu_msg = Vector3()
        imu_accel = False

        # Extract data from message
        for accelerometer in accelerometers:
            name = accelerometer.name
            value = accelerometer.value
            if name == "Accelerometer":
                imu_accel = True
                imu_msg.x = value.X
                imu_msg.y = value.Y
                imu_msg.z = value.Z
            else:
                rospy.logwarn(f"Unknown accelerometer: '{name}'", logger_name="rc_api")

        if imu_accel:
            # Make sure that acceleration is not completely zero or we will get error in filter.
            # Happens if robot is moved manually in the simulation
            if imu_msg.x == 0 and imu_msg.y == 0 and imu_msg.z == 0:
                imu_msg.z = 0.001

            self.pub_imu.publish(imu_msg)

    def handle_camera_measurements(self, cameras):
        for camera in cameras:
            name = camera.name
            if name == "Camera":
                width = camera.width
                height = camera.height
                quality = camera.quality  # 1 = raw image, 100 = no compression, 0 = high compression
                image = camera.image  # RAW or JPEG encoded data (note: JPEG is not yet implemented)

                if not self.published_camera_info:  # Publish CameraInfo once, it will be latched
                    self.publish_camera_info(height, width)
                    self.published_camera_info = True

                img_msg = Image()
                img_msg.header.stamp = self.stamp
                img_msg.height = height
                img_msg.width = width
                img_msg.encoding = "bgr8"
                img_msg.step = 3 * width
                img_msg.data = image
                self.pub_camera.publish(img_msg)
            else:
                rospy.logwarn(f"Unknown camera: '{name}'", logger_name="rc_api")

    def publish_camera_info(self, height, width):
        camera_info_msg = CameraInfo()
        camera_info_msg.header.stamp = self.stamp
        camera_info_msg.height = height
        camera_info_msg.width = width
        f_y = self.mat_from_fov_and_resolution(
            self.h_fov_to_v_fov(self.camera_FOV, height, width),
            height)
        f_x = self.mat_from_fov_and_resolution(self.camera_FOV, width)
        camera_info_msg.K = [f_x, 0, width / 2,
                        0, f_y, height / 2,
                        0, 0, 1]
        camera_info_msg.P = [f_x, 0, width / 2, 0,
                        0, f_y, height / 2, 0,
                        0, 0, 1, 0]
        self.pub_camera_info.publish(camera_info_msg)

    def mat_from_fov_and_resolution(self, fov, res):
        return 0.5 * res * (math.cos((fov / 2)) / math.sin((fov / 2)))

    def h_fov_to_v_fov(self, h_fov, height, width):
        return 2 * math.atan(math.tan(h_fov * 0.5) * (height / width))

    def handle_position_sensor_measurements(self, position_sensors):
        state_msg = JointState()
        state_msg.header.stamp = self.stamp
        for position_sensor in position_sensors:
            state_msg.name.append(self.webots_to_joint(position_sensor.name))
            state_msg.position.append(position_sensor.value)
        self.pub_joint_states.publish(state_msg)

    def get_sensor_time_steps(self, active=True):
        sensor_time_steps = []
        for sensor_name in self.sensors_names:
            time_step = 8
            if sensor_name == "Camera":
                time_step = 16
            if not active:
                time_step = 0
            sensor_time_step = messages_pb2.SensorTimeStep()
            sensor_time_step.name = sensor_name
            sensor_time_step.timeStep = time_step
            sensor_time_steps.append(sensor_time_step)
        return sensor_time_steps

    #Aqui a magica comeca a acontecer
    def send_actuator_requests(self, sensor_time_steps=None):
        actuator_requests = messages_pb2.ActuatorRequests()
        if sensor_time_steps is not None:
            actuator_requests.sensor_time_steps.extend(sensor_time_steps)

        # Makes this this thread safe
        with self.joint_command_mutex:
            joint_command = copy.deepcopy(self.joint_command)
        
        for i, name in enumerate(joint_command.motor_name):

            motor_position = messages_pb2.MotorPosition()
            motor_position.name = self.joint_to_webots(name)
            motor_position.position = joint_command.position[i]
            actuator_requests.motor_positions.append(motor_position)
            motor_velocity = messages_pb2.MotorVelocity()
            motor_velocity.name = self.joint_to_webots(name)

            if len(joint_command.velocity) == 0 or joint_command.velocity[i] == -1:
                motor_velocity.velocity = 2
            else:
                motor_velocity.velocity = joint_command.velocity[i]
            
            actuator_requests.motor_velocities.append(motor_velocity)    

        # Aqui a magica acontece
        msg = actuator_requests.SerializeToString()
        msg_size = struct.pack(">L", len(msg))
        self.socket.send(msg_size + msg)

    def joint_to_webots(self, joint):
        '''
        if joint in ('LLEG_1', 'RLEG_1'):
            return joint + '[hip]'
        elif joint in ('LARM_0', 'RARM_0'):
            return joint + '[shoulder]'
        else:
        '''
        return joint

    def webots_to_joint(self, name):
        return re.sub(r'( \[\w+\])?_sensor', '', name)

if __name__ == '__main__':
    NatashaApi()
