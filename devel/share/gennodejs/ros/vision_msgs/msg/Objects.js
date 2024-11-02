// Auto-generated. Do not edit!

// (in-package vision_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Ball = require('./Ball.js');
let Goal = require('./Goal.js');
let Robot = require('./Robot.js');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class Objects {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ball = null;
      this.goal = null;
      this.robots = null;
      this.image = null;
    }
    else {
      if (initObj.hasOwnProperty('ball')) {
        this.ball = initObj.ball
      }
      else {
        this.ball = new Ball();
      }
      if (initObj.hasOwnProperty('goal')) {
        this.goal = initObj.goal
      }
      else {
        this.goal = new Goal();
      }
      if (initObj.hasOwnProperty('robots')) {
        this.robots = initObj.robots
      }
      else {
        this.robots = [];
      }
      if (initObj.hasOwnProperty('image')) {
        this.image = initObj.image
      }
      else {
        this.image = new sensor_msgs.msg.Image();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Objects
    // Serialize message field [ball]
    bufferOffset = Ball.serialize(obj.ball, buffer, bufferOffset);
    // Serialize message field [goal]
    bufferOffset = Goal.serialize(obj.goal, buffer, bufferOffset);
    // Serialize message field [robots]
    // Serialize the length for message field [robots]
    bufferOffset = _serializer.uint32(obj.robots.length, buffer, bufferOffset);
    obj.robots.forEach((val) => {
      bufferOffset = Robot.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [image]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.image, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Objects
    let len;
    let data = new Objects(null);
    // Deserialize message field [ball]
    data.ball = Ball.deserialize(buffer, bufferOffset);
    // Deserialize message field [goal]
    data.goal = Goal.deserialize(buffer, bufferOffset);
    // Deserialize message field [robots]
    // Deserialize array length for message field [robots]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.robots = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.robots[i] = Robot.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [image]
    data.image = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.robots.length;
    length += sensor_msgs.msg.Image.getMessageSize(object.image);
    return length + 30;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vision_msgs/Objects';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '19f71dba810720091bb37489652c025c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    vision_msgs/Ball ball
    vision_msgs/Goal goal
    vision_msgs/Robot[] robots
    sensor_msgs/Image image
    ================================================================================
    MSG: vision_msgs/Ball
    bool found
    int32 x
    int32 y
    int32 roi_width
    int32 roi_height
    ================================================================================
    MSG: vision_msgs/Goal
    bool found
    int32 x
    int32 y
    ================================================================================
    MSG: vision_msgs/Robot
    int32 x
    int32 y
    ================================================================================
    MSG: sensor_msgs/Image
    # This message contains an uncompressed image
    # (0, 0) is at top-left corner of image
    #
    
    Header header        # Header timestamp should be acquisition time of image
                         # Header frame_id should be optical frame of camera
                         # origin of frame should be optical center of camera
                         # +x should point to the right in the image
                         # +y should point down in the image
                         # +z should point into to plane of the image
                         # If the frame_id here and the frame_id of the CameraInfo
                         # message associated with the image conflict
                         # the behavior is undefined
    
    uint32 height         # image height, that is, number of rows
    uint32 width          # image width, that is, number of columns
    
    # The legal values for encoding are in file src/image_encodings.cpp
    # If you want to standardize a new string format, join
    # ros-users@lists.sourceforge.net and send an email proposing a new encoding.
    
    string encoding       # Encoding of pixels -- channel meaning, ordering, size
                          # taken from the list of strings in include/sensor_msgs/image_encodings.h
    
    uint8 is_bigendian    # is this data bigendian?
    uint32 step           # Full row length in bytes
    uint8[] data          # actual matrix data, size is (step * rows)
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Objects(null);
    if (msg.ball !== undefined) {
      resolved.ball = Ball.Resolve(msg.ball)
    }
    else {
      resolved.ball = new Ball()
    }

    if (msg.goal !== undefined) {
      resolved.goal = Goal.Resolve(msg.goal)
    }
    else {
      resolved.goal = new Goal()
    }

    if (msg.robots !== undefined) {
      resolved.robots = new Array(msg.robots.length);
      for (let i = 0; i < resolved.robots.length; ++i) {
        resolved.robots[i] = Robot.Resolve(msg.robots[i]);
      }
    }
    else {
      resolved.robots = []
    }

    if (msg.image !== undefined) {
      resolved.image = sensor_msgs.msg.Image.Resolve(msg.image)
    }
    else {
      resolved.image = new sensor_msgs.msg.Image()
    }

    return resolved;
    }
};

module.exports = Objects;
