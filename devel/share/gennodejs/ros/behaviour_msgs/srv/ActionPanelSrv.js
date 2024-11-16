// Auto-generated. Do not edit!

// (in-package behaviour_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ActionMsg = require('../msg/ActionMsg.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class ActionPanelSrvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.actions = null;
    }
    else {
      if (initObj.hasOwnProperty('actions')) {
        this.actions = initObj.actions
      }
      else {
        this.actions = new ActionMsg();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionPanelSrvRequest
    // Serialize message field [actions]
    bufferOffset = ActionMsg.serialize(obj.actions, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionPanelSrvRequest
    let len;
    let data = new ActionPanelSrvRequest(null);
    // Deserialize message field [actions]
    data.actions = ActionMsg.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 11;
  }

  static datatype() {
    // Returns string type for a service object
    return 'behaviour_msgs/ActionPanelSrvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c602a34772abebfb14617e6bc6021cd0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    behaviour_msgs/ActionMsg actions
    
    
    ================================================================================
    MSG: behaviour_msgs/ActionMsg
    
    bool ball_tracking
    bool center_ball
    bool align_body
    bool walk
    bool kick
    int32 defend
    bool squat
    bool goal_tracking
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionPanelSrvRequest(null);
    if (msg.actions !== undefined) {
      resolved.actions = ActionMsg.Resolve(msg.actions)
    }
    else {
      resolved.actions = new ActionMsg()
    }

    return resolved;
    }
};

class ActionPanelSrvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.status = null;
    }
    else {
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionPanelSrvResponse
    // Serialize message field [status]
    bufferOffset = _serializer.bool(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionPanelSrvResponse
    let len;
    let data = new ActionPanelSrvResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'behaviour_msgs/ActionPanelSrvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3a1255d4d998bd4d6585c64639b5ee9a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool status
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionPanelSrvResponse(null);
    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = false
    }

    return resolved;
    }
};

module.exports = {
  Request: ActionPanelSrvRequest,
  Response: ActionPanelSrvResponse,
  md5sum() { return '08e9f2a38a830622970eb20f373e5093'; },
  datatype() { return 'behaviour_msgs/ActionPanelSrv'; }
};
