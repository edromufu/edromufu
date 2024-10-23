// Auto-generated. Do not edit!

// (in-package vision_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Rightgoalpost {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.found = null;
      this.x = null;
      this.y = null;
      this.roi_width = null;
      this.roi_height = null;
    }
    else {
      if (initObj.hasOwnProperty('found')) {
        this.found = initObj.found
      }
      else {
        this.found = false;
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('roi_width')) {
        this.roi_width = initObj.roi_width
      }
      else {
        this.roi_width = 0;
      }
      if (initObj.hasOwnProperty('roi_height')) {
        this.roi_height = initObj.roi_height
      }
      else {
        this.roi_height = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Rightgoalpost
    // Serialize message field [found]
    bufferOffset = _serializer.bool(obj.found, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = _serializer.int32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int32(obj.y, buffer, bufferOffset);
    // Serialize message field [roi_width]
    bufferOffset = _serializer.int32(obj.roi_width, buffer, bufferOffset);
    // Serialize message field [roi_height]
    bufferOffset = _serializer.int32(obj.roi_height, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Rightgoalpost
    let len;
    let data = new Rightgoalpost(null);
    // Deserialize message field [found]
    data.found = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [roi_width]
    data.roi_width = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [roi_height]
    data.roi_height = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 17;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vision_msgs/Rightgoalpost';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '593e6a8c66231b4fe6d1d33cf452902c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new Rightgoalpost(null);
    if (msg.found !== undefined) {
      resolved.found = msg.found;
    }
    else {
      resolved.found = false
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.roi_width !== undefined) {
      resolved.roi_width = msg.roi_width;
    }
    else {
      resolved.roi_width = 0
    }

    if (msg.roi_height !== undefined) {
      resolved.roi_height = msg.roi_height;
    }
    else {
      resolved.roi_height = 0
    }

    return resolved;
    }
};

module.exports = Rightgoalpost;
