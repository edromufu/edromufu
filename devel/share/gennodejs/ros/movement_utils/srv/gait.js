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

class gaitRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.steps_number = null;
      this.step_height = null;
    }
    else {
      if (initObj.hasOwnProperty('steps_number')) {
        this.steps_number = initObj.steps_number
      }
      else {
        this.steps_number = 0;
      }
      if (initObj.hasOwnProperty('step_height')) {
        this.step_height = initObj.step_height
      }
      else {
        this.step_height = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type gaitRequest
    // Serialize message field [steps_number]
    bufferOffset = _serializer.int8(obj.steps_number, buffer, bufferOffset);
    // Serialize message field [step_height]
    bufferOffset = _serializer.float32(obj.step_height, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gaitRequest
    let len;
    let data = new gaitRequest(null);
    // Deserialize message field [steps_number]
    data.steps_number = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [step_height]
    data.step_height = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_utils/gaitRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '80c470ae217144d053d06dd858989a2f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 steps_number
    float32 step_height
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new gaitRequest(null);
    if (msg.steps_number !== undefined) {
      resolved.steps_number = msg.steps_number;
    }
    else {
      resolved.steps_number = 0
    }

    if (msg.step_height !== undefined) {
      resolved.step_height = msg.step_height;
    }
    else {
      resolved.step_height = 0.0
    }

    return resolved;
    }
};

class gaitResponse {
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
    // Serializes a message object of type gaitResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gaitResponse
    let len;
    let data = new gaitResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_utils/gaitResponse';
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
    const resolved = new gaitResponse(null);
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
  Request: gaitRequest,
  Response: gaitResponse,
  md5sum() { return '372f208eec6910dde42b51ee38202481'; },
  datatype() { return 'movement_utils/gait'; }
};
