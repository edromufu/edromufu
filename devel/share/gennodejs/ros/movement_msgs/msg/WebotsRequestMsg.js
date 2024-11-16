// Auto-generated. Do not edit!

// (in-package movement_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class WebotsRequestMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motors_position = null;
      this.motors_velocity = null;
    }
    else {
      if (initObj.hasOwnProperty('motors_position')) {
        this.motors_position = initObj.motors_position
      }
      else {
        this.motors_position = new Array(20).fill(0);
      }
      if (initObj.hasOwnProperty('motors_velocity')) {
        this.motors_velocity = initObj.motors_velocity
      }
      else {
        this.motors_velocity = new Array(20).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WebotsRequestMsg
    // Check that the constant length array field [motors_position] has the right length
    if (obj.motors_position.length !== 20) {
      throw new Error('Unable to serialize array field motors_position - length must be 20')
    }
    // Serialize message field [motors_position]
    bufferOffset = _arraySerializer.float32(obj.motors_position, buffer, bufferOffset, 20);
    // Check that the constant length array field [motors_velocity] has the right length
    if (obj.motors_velocity.length !== 20) {
      throw new Error('Unable to serialize array field motors_velocity - length must be 20')
    }
    // Serialize message field [motors_velocity]
    bufferOffset = _arraySerializer.float32(obj.motors_velocity, buffer, bufferOffset, 20);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WebotsRequestMsg
    let len;
    let data = new WebotsRequestMsg(null);
    // Deserialize message field [motors_position]
    data.motors_position = _arrayDeserializer.float32(buffer, bufferOffset, 20)
    // Deserialize message field [motors_velocity]
    data.motors_velocity = _arrayDeserializer.float32(buffer, bufferOffset, 20)
    return data;
  }

  static getMessageSize(object) {
    return 160;
  }

  static datatype() {
    // Returns string type for a message object
    return 'movement_msgs/WebotsRequestMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3463d5e3ddb49315fab6bfa4cde9cb44';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[20] motors_position
    float32[20] motors_velocity
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WebotsRequestMsg(null);
    if (msg.motors_position !== undefined) {
      resolved.motors_position = msg.motors_position;
    }
    else {
      resolved.motors_position = new Array(20).fill(0)
    }

    if (msg.motors_velocity !== undefined) {
      resolved.motors_velocity = msg.motors_velocity;
    }
    else {
      resolved.motors_velocity = new Array(20).fill(0)
    }

    return resolved;
    }
};

module.exports = WebotsRequestMsg;
