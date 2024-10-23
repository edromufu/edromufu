// Auto-generated. Do not edit!

// (in-package movement_utils.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class walk_forwardRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.support_foot = null;
      this.steps_number = null;
    }
    else {
      if (initObj.hasOwnProperty('support_foot')) {
        this.support_foot = initObj.support_foot
      }
      else {
        this.support_foot = 0;
      }
      if (initObj.hasOwnProperty('steps_number')) {
        this.steps_number = initObj.steps_number
      }
      else {
        this.steps_number = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type walk_forwardRequest
    // Serialize message field [support_foot]
    bufferOffset = _serializer.int8(obj.support_foot, buffer, bufferOffset);
    // Serialize message field [steps_number]
    bufferOffset = _serializer.int8(obj.steps_number, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type walk_forwardRequest
    let len;
    let data = new walk_forwardRequest(null);
    // Deserialize message field [support_foot]
    data.support_foot = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [steps_number]
    data.steps_number = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_utils/walk_forwardRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e0911cfa143d6da846959597e9cd226e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 support_foot
    int8 steps_number
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new walk_forwardRequest(null);
    if (msg.support_foot !== undefined) {
      resolved.support_foot = msg.support_foot;
    }
    else {
      resolved.support_foot = 0
    }

    if (msg.steps_number !== undefined) {
      resolved.steps_number = msg.steps_number;
    }
    else {
      resolved.steps_number = 0
    }

    return resolved;
    }
};

class walk_forwardResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type walk_forwardResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type walk_forwardResponse
    let len;
    let data = new walk_forwardResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_utils/walk_forwardResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new walk_forwardResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: walk_forwardRequest,
  Response: walk_forwardResponse,
  md5sum() { return '4e96d691545ef71c6c6ffe49fb624ea4'; },
  datatype() { return 'movement_utils/walk_forward'; }
};
