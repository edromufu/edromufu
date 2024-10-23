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

class stateMachineMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ballPosition = null;
      this.ballClose = null;
      this.ballFound = null;
      this.fallState = null;
      this.horMotorOutOfCenter = null;
      this.headKickCheck = null;
    }
    else {
      if (initObj.hasOwnProperty('ballPosition')) {
        this.ballPosition = initObj.ballPosition
      }
      else {
        this.ballPosition = '';
      }
      if (initObj.hasOwnProperty('ballClose')) {
        this.ballClose = initObj.ballClose
      }
      else {
        this.ballClose = false;
      }
      if (initObj.hasOwnProperty('ballFound')) {
        this.ballFound = initObj.ballFound
      }
      else {
        this.ballFound = false;
      }
      if (initObj.hasOwnProperty('fallState')) {
        this.fallState = initObj.fallState
      }
      else {
        this.fallState = '';
      }
      if (initObj.hasOwnProperty('horMotorOutOfCenter')) {
        this.horMotorOutOfCenter = initObj.horMotorOutOfCenter
      }
      else {
        this.horMotorOutOfCenter = '';
      }
      if (initObj.hasOwnProperty('headKickCheck')) {
        this.headKickCheck = initObj.headKickCheck
      }
      else {
        this.headKickCheck = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type stateMachineMsg
    // Serialize message field [ballPosition]
    bufferOffset = _serializer.string(obj.ballPosition, buffer, bufferOffset);
    // Serialize message field [ballClose]
    bufferOffset = _serializer.bool(obj.ballClose, buffer, bufferOffset);
    // Serialize message field [ballFound]
    bufferOffset = _serializer.bool(obj.ballFound, buffer, bufferOffset);
    // Serialize message field [fallState]
    bufferOffset = _serializer.string(obj.fallState, buffer, bufferOffset);
    // Serialize message field [horMotorOutOfCenter]
    bufferOffset = _serializer.string(obj.horMotorOutOfCenter, buffer, bufferOffset);
    // Serialize message field [headKickCheck]
    bufferOffset = _serializer.bool(obj.headKickCheck, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type stateMachineMsg
    let len;
    let data = new stateMachineMsg(null);
    // Deserialize message field [ballPosition]
    data.ballPosition = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [ballClose]
    data.ballClose = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ballFound]
    data.ballFound = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [fallState]
    data.fallState = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [horMotorOutOfCenter]
    data.horMotorOutOfCenter = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [headKickCheck]
    data.headKickCheck = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.ballPosition);
    length += _getByteLength(object.fallState);
    length += _getByteLength(object.horMotorOutOfCenter);
    return length + 15;
  }

  static datatype() {
    // Returns string type for a message object
    return 'modularized_bhv_msgs/stateMachineMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c591d7d3c44206a23a253ed3e26e96da';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string ballPosition
    bool ballClose
    bool ballFound
    string fallState
    string horMotorOutOfCenter
    bool headKickCheck
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new stateMachineMsg(null);
    if (msg.ballPosition !== undefined) {
      resolved.ballPosition = msg.ballPosition;
    }
    else {
      resolved.ballPosition = ''
    }

    if (msg.ballClose !== undefined) {
      resolved.ballClose = msg.ballClose;
    }
    else {
      resolved.ballClose = false
    }

    if (msg.ballFound !== undefined) {
      resolved.ballFound = msg.ballFound;
    }
    else {
      resolved.ballFound = false
    }

    if (msg.fallState !== undefined) {
      resolved.fallState = msg.fallState;
    }
    else {
      resolved.fallState = ''
    }

    if (msg.horMotorOutOfCenter !== undefined) {
      resolved.horMotorOutOfCenter = msg.horMotorOutOfCenter;
    }
    else {
      resolved.horMotorOutOfCenter = ''
    }

    if (msg.headKickCheck !== undefined) {
      resolved.headKickCheck = msg.headKickCheck;
    }
    else {
      resolved.headKickCheck = false
    }

    return resolved;
    }
};

module.exports = stateMachineMsg;
