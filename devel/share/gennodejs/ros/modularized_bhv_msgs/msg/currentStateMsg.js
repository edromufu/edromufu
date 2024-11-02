// Auto-generated. Do not edit!

// (in-package modularized_bhv_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class currentStateMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.currentState = null;
    }
    else {
      if (initObj.hasOwnProperty('currentState')) {
        this.currentState = initObj.currentState
      }
      else {
        this.currentState = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type currentStateMsg
    // Serialize message field [currentState]
    bufferOffset = _serializer.string(obj.currentState, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type currentStateMsg
    let len;
    let data = new currentStateMsg(null);
    // Deserialize message field [currentState]
    data.currentState = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.currentState);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'modularized_bhv_msgs/currentStateMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '51b88f6d6df0913c6465fdbbb69a8c4e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string currentState
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new currentStateMsg(null);
    if (msg.currentState !== undefined) {
      resolved.currentState = msg.currentState;
    }
    else {
      resolved.currentState = ''
    }

    return resolved;
    }
};

module.exports = currentStateMsg;
