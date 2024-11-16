// Auto-generated. Do not edit!

// (in-package modularized_bhv_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class moveRequestRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.moveRequest = null;
    }
    else {
      if (initObj.hasOwnProperty('moveRequest')) {
        this.moveRequest = initObj.moveRequest
      }
      else {
        this.moveRequest = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type moveRequestRequest
    // Serialize message field [moveRequest]
    bufferOffset = _serializer.string(obj.moveRequest, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type moveRequestRequest
    let len;
    let data = new moveRequestRequest(null);
    // Deserialize message field [moveRequest]
    data.moveRequest = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.moveRequest);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'modularized_bhv_msgs/moveRequestRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b133e08dd2bfaecedf3ed6e116063474';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string moveRequest
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new moveRequestRequest(null);
    if (msg.moveRequest !== undefined) {
      resolved.moveRequest = msg.moveRequest;
    }
    else {
      resolved.moveRequest = ''
    }

    return resolved;
    }
};

class moveRequestResponse {
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
    // Serializes a message object of type moveRequestResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type moveRequestResponse
    let len;
    let data = new moveRequestResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'modularized_bhv_msgs/moveRequestResponse';
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
    const resolved = new moveRequestResponse(null);
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
  Request: moveRequestRequest,
  Response: moveRequestResponse,
  md5sum() { return 'fa4c3676b8fc489dd65422b45b94f727'; },
  datatype() { return 'modularized_bhv_msgs/moveRequest'; }
};
