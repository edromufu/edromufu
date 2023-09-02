import serial
import json
import rospy

imu = serial.Serial('/dev/ttyUSB0', 9600)
imupub=rospy.Publisher('/sensor_imu', stateMachineMsg, queue_size=1)
def talker():
    cc = str(imu.readline())

    cleaned_str = str(cc[2:][:-5])
    try:
        [angleX, angleY, angleZ] = cleaned_str.split(",")
    except:
        [angleX, angleY, angleZ] = [-9999,-9999,-9999]
        
    print('angleX: ', angleX, ' angleY: ', angleY, ' angleZ: ', angleZ)

while 1:
    talker()

imu.close()