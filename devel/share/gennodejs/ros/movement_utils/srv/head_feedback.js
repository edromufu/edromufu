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

class head_feedbackRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dont_use = null;
    }
    else {
      if (initObj.hasOwnProperty('dont_use')) {
        this.dont_use = initObj.dont_use
      }
      else {
        this.dont_use = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type head_feedbackRequest
    // Serialize message field [dont_use]
    bufferOffset = _serializer.bool(obj.dont_use, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type head_feedbackRequest
    let len;
    let data = new head_feedbackRequest(null);
    // Deserialize message field [dont_use]
    data.dont_use = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_utils/head_feedbackRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e681e4699d32e2108cfd7b961bdbeafa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool dont_use
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new head_feedbackRequest(null);
    if (msg.dont_use !== undefined) {
      resolved.dont_use = msg.dont_use;
    }
    else {
      resolved.dont_use = false
    }

    return resolved;
    }
};

class head_feedbackResponse {
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
        this.pos_vector = new Array(2).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type head_feedbackResponse
    // Check that the constant length array field [pos_vector] has the right length
    if (obj.pos_vector.length !== 2) {
      throw new Error('Unable to serialize array field pos_vector - length must be 2')
    }
    // Serialize message field [pos_vector]
    bufferOffset = _arraySerializer.float32(obj.pos_vector, buffer, bufferOffset, 2);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type head_feedbackResponse
    let len;
    let data = new head_feedbackResponse(null);
    // Deserialize message field [pos_vector]
    data.pos_vector = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_utils/head_feedbackResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '019f44c03fbd0840875f997c96bee773';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[2] pos_vector
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new head_feedbackResponse(null);
    if (msg.pos_vector !== undefined) {
      resolved.pos_vector = msg.pos_vector;
    }
    else {
      resolved.pos_vector = new Array(2).fill(0)
    }

    return resolved;
    }
};

module.exports = {
  Request: head_feedbackRequest,
  Response: head_feedbackResponse,
  md5sum() { return 'a254b821d70340d5ccc8779b3f5e7d9c'; },
  datatype() { return 'movement_utils/head_feedback'; }
};
