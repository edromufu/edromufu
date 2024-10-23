// Auto-generated. Do not edit!

// (in-package behaviour_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class GameControllerSrvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.host = null;
      this.port = null;
    }
    else {
      if (initObj.hasOwnProperty('host')) {
        this.host = initObj.host
      }
      else {
        this.host = '';
      }
      if (initObj.hasOwnProperty('port')) {
        this.port = initObj.port
      }
      else {
        this.port = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GameControllerSrvRequest
    // Serialize message field [host]
    bufferOffset = _serializer.string(obj.host, buffer, bufferOffset);
    // Serialize message field [port]
    bufferOffset = _serializer.int32(obj.port, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GameControllerSrvRequest
    let len;
    let data = new GameControllerSrvRequest(null);
    // Deserialize message field [host]
    data.host = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [port]
    data.port = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.host);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'behaviour_msgs/GameControllerSrvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '55932133259e8c3335a553618447da45';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string host
    int32 port
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GameControllerSrvRequest(null);
    if (msg.host !== undefined) {
      resolved.host = msg.host;
    }
    else {
      resolved.host = ''
    }

    if (msg.port !== undefined) {
      resolved.port = msg.port;
    }
    else {
      resolved.port = 0
    }

    return resolved;
    }
};

class GameControllerSrvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GameControllerSrvResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GameControllerSrvResponse
    let len;
    let data = new GameControllerSrvResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'behaviour_msgs/GameControllerSrvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GameControllerSrvResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: GameControllerSrvRequest,
  Response: GameControllerSrvResponse,
  md5sum() { return '55932133259e8c3335a553618447da45'; },
  datatype() { return 'behaviour_msgs/GameControllerSrv'; }
};
