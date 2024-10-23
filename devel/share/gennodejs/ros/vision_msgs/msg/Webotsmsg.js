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
let Leftgoalpost = require('./Leftgoalpost.js');
let Rightgoalpost = require('./Rightgoalpost.js');

//-----------------------------------------------------------

class Webotsmsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.searching = null;
      this.fps = null;
      this.ball = null;
      this.leftgoalpost = null;
      this.rightgoalpost = null;
    }
    else {
      if (initObj.hasOwnProperty('searching')) {
        this.searching = initObj.searching
      }
      else {
        this.searching = false;
      }
      if (initObj.hasOwnProperty('fps')) {
        this.fps = initObj.fps
      }
      else {
        this.fps = 0;
      }
      if (initObj.hasOwnProperty('ball')) {
        this.ball = initObj.ball
      }
      else {
        this.ball = new Ball();
      }
      if (initObj.hasOwnProperty('leftgoalpost')) {
        this.leftgoalpost = initObj.leftgoalpost
      }
      else {
        this.leftgoalpost = new Leftgoalpost();
      }
      if (initObj.hasOwnProperty('rightgoalpost')) {
        this.rightgoalpost = initObj.rightgoalpost
      }
      else {
        this.rightgoalpost = new Rightgoalpost();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Webotsmsg
    // Serialize message field [searching]
    bufferOffset = _serializer.bool(obj.searching, buffer, bufferOffset);
    // Serialize message field [fps]
    bufferOffset = _serializer.uint8(obj.fps, buffer, bufferOffset);
    // Serialize message field [ball]
    bufferOffset = Ball.serialize(obj.ball, buffer, bufferOffset);
    // Serialize message field [leftgoalpost]
    bufferOffset = Leftgoalpost.serialize(obj.leftgoalpost, buffer, bufferOffset);
    // Serialize message field [rightgoalpost]
    bufferOffset = Rightgoalpost.serialize(obj.rightgoalpost, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Webotsmsg
    let len;
    let data = new Webotsmsg(null);
    // Deserialize message field [searching]
    data.searching = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [fps]
    data.fps = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ball]
    data.ball = Ball.deserialize(buffer, bufferOffset);
    // Deserialize message field [leftgoalpost]
    data.leftgoalpost = Leftgoalpost.deserialize(buffer, bufferOffset);
    // Deserialize message field [rightgoalpost]
    data.rightgoalpost = Rightgoalpost.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 53;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vision_msgs/Webotsmsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2b9c0baf80135ab319a9a2d5f79a6c9a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool searching
    uint8 fps
    vision_msgs/Ball ball
    vision_msgs/Leftgoalpost leftgoalpost
    vision_msgs/Rightgoalpost rightgoalpost
    ================================================================================
    MSG: vision_msgs/Ball
    bool found
    int32 x
    int32 y
    int32 roi_width
    int32 roi_height
    ================================================================================
    MSG: vision_msgs/Leftgoalpost
    bool found
    int32 x
    int32 y
    int32 roi_width
    int32 roi_height
    
    ================================================================================
    MSG: vision_msgs/Rightgoalpost
    bool found
    int32 x
    int32 y
    int32 roi_width
    int32 roi_height
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Webotsmsg(null);
    if (msg.searching !== undefined) {
      resolved.searching = msg.searching;
    }
    else {
      resolved.searching = false
    }

    if (msg.fps !== undefined) {
      resolved.fps = msg.fps;
    }
    else {
      resolved.fps = 0
    }

    if (msg.ball !== undefined) {
      resolved.ball = Ball.Resolve(msg.ball)
    }
    else {
      resolved.ball = new Ball()
    }

    if (msg.leftgoalpost !== undefined) {
      resolved.leftgoalpost = Leftgoalpost.Resolve(msg.leftgoalpost)
    }
    else {
      resolved.leftgoalpost = new Leftgoalpost()
    }

    if (msg.rightgoalpost !== undefined) {
      resolved.rightgoalpost = Rightgoalpost.Resolve(msg.rightgoalpost)
    }
    else {
      resolved.rightgoalpost = new Rightgoalpost()
    }

    return resolved;
    }
};

module.exports = Webotsmsg;
