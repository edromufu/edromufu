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

class ApprovedMovementMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.approved_movement = null;
    }
    else {
      if (initObj.hasOwnProperty('approved_movement')) {
        this.approved_movement = initObj.approved_movement
      }
      else {
        this.approved_movement = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ApprovedMovementMsg
    // Serialize message field [approved_movement]
    bufferOffset = _serializer.string(obj.approved_movement, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ApprovedMovementMsg
    let len;
    let data = new ApprovedMovementMsg(null);
    // Deserialize message field [approved_movement]
    data.approved_movement = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.approved_movement);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'movement_msgs/ApprovedMovementMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '255fbce3bb4374d8b5382cbf8e9f1840';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string approved_movement
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ApprovedMovementMsg(null);
    if (msg.approved_movement !== undefined) {
      resolved.approved_movement = msg.approved_movement;
    }
    else {
      resolved.approved_movement = ''
    }

    return resolved;
    }
};

module.exports = ApprovedMovementMsg;
