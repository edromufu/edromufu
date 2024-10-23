// Auto-generated. Do not edit!

// (in-package movement_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class BehRequestSrvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.required_movement = null;
      this.required_status = null;
    }
    else {
      if (initObj.hasOwnProperty('required_movement')) {
        this.required_movement = initObj.required_movement
      }
      else {
        this.required_movement = '';
      }
      if (initObj.hasOwnProperty('required_status')) {
        this.required_status = initObj.required_status
      }
      else {
        this.required_status = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BehRequestSrvRequest
    // Serialize message field [required_movement]
    bufferOffset = _serializer.string(obj.required_movement, buffer, bufferOffset);
    // Serialize message field [required_status]
    bufferOffset = _serializer.bool(obj.required_status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BehRequestSrvRequest
    let len;
    let data = new BehRequestSrvRequest(null);
    // Deserialize message field [required_movement]
    data.required_movement = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [required_status]
    data.required_status = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.required_movement);
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_msgs/BehRequestSrvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a8e8e1d113594f935b637fde0165e779';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string required_movement
    bool required_status
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BehRequestSrvRequest(null);
    if (msg.required_movement !== undefined) {
      resolved.required_movement = msg.required_movement;
    }
    else {
      resolved.required_movement = ''
    }

    if (msg.required_status !== undefined) {
      resolved.required_status = msg.required_status;
    }
    else {
      resolved.required_status = false
    }

    return resolved;
    }
};

class BehRequestSrvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.response = null;
    }
    else {
      if (initObj.hasOwnProperty('response')) {
        this.response = initObj.response
      }
      else {
        this.response = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BehRequestSrvResponse
    // Serialize message field [response]
    bufferOffset = _serializer.bool(obj.response, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BehRequestSrvResponse
    let len;
    let data = new BehRequestSrvResponse(null);
    // Deserialize message field [response]
    data.response = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_msgs/BehRequestSrvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '003b81baa95ab323fc1ddf3c7d0bee81';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    bool response
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BehRequestSrvResponse(null);
    if (msg.response !== undefined) {
      resolved.response = msg.response;
    }
    else {
      resolved.response = false
    }

    return resolved;
    }
};

module.exports = {
  Request: BehRequestSrvRequest,
  Response: BehRequestSrvResponse,
  md5sum() { return '4f5d36d25e04a31db12adbc950d9b1a5'; },
  datatype() { return 'movement_msgs/BehRequestSrv'; }
};
