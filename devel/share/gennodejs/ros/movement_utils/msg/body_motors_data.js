// Auto-generated. Do not edit!

// (in-package movement_utils.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class body_motors_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pos_vector = null;
    }
    else {
      if (initObj.hasOwnProperty('pos_vector')) {
        this.pos_vector = initObj.pos_vector
      }
      else {
        this.pos_vector = new Array(18).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type body_motors_data
    // Check that the constant length array field [pos_vector] has the right length
    if (obj.pos_vector.length !== 18) {
      throw new Error('Unable to serialize array field pos_vector - length must be 18')
    }
    // Serialize message field [pos_vector]
    bufferOffset = _arraySerializer.float32(obj.pos_vector, buffer, bufferOffset, 18);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type body_motors_data
    let len;
    let data = new body_motors_data(null);
    // Deserialize message field [pos_vector]
    data.pos_vector = _arrayDeserializer.float32(buffer, bufferOffset, 18)
    return data;
  }

  static getMessageSize(object) {
    return 72;
  }

  static datatype() {
    // Returns string type for a message object
    return 'movement_utils/body_motors_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '18af1fa9d2e7d06f4ff52d42169a41bd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[18] pos_vector
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new body_motors_data(null);
    if (msg.pos_vector !== undefined) {
      resolved.pos_vector = msg.pos_vector;
    }
    else {
      resolved.pos_vector = new Array(18).fill(0)
    }

    return resolved;
    }
};

module.exports = body_motors_data;
