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

class WalkTestParametersSrvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.currentWalk = null;
      this.stepGain = null;
      this.lateralGain = null;
      this.turnGain = null;
      this.freq = null;
      this.supportPhaseRatio = null;
      this.footYOffset = null;
      this.riseGain = null;
      this.trunkZOffset = null;
      this.swingGain = null;
      this.swingRollGain = null;
      this.swingPhase = null;
      this.stepUpVel = null;
      this.stepDownVel = null;
      this.riseUpVel = null;
      this.riseDownVel = null;
      this.swingPause = null;
      this.swingVel = null;
      this.trunkXOffset = null;
      this.trunkYOffset = null;
      this.trunkPitch = null;
      this.trunkRoll = null;
      this.extraLeftX = null;
      this.extraLeftY = null;
      this.extraLeftZ = null;
      this.extraRightX = null;
      this.extraRightY = null;
      this.extraRightZ = null;
      this.extraLeftYaw = null;
      this.extraLeftPitch = null;
      this.extraLeftRoll = null;
      this.extraRightYaw = null;
      this.extraRightPitch = null;
      this.extraRightRoll = null;
    }
    else {
      if (initObj.hasOwnProperty('currentWalk')) {
        this.currentWalk = initObj.currentWalk
      }
      else {
        this.currentWalk = '';
      }
      if (initObj.hasOwnProperty('stepGain')) {
        this.stepGain = initObj.stepGain
      }
      else {
        this.stepGain = 0.0;
      }
      if (initObj.hasOwnProperty('lateralGain')) {
        this.lateralGain = initObj.lateralGain
      }
      else {
        this.lateralGain = 0.0;
      }
      if (initObj.hasOwnProperty('turnGain')) {
        this.turnGain = initObj.turnGain
      }
      else {
        this.turnGain = 0.0;
      }
      if (initObj.hasOwnProperty('freq')) {
        this.freq = initObj.freq
      }
      else {
        this.freq = 0.0;
      }
      if (initObj.hasOwnProperty('supportPhaseRatio')) {
        this.supportPhaseRatio = initObj.supportPhaseRatio
      }
      else {
        this.supportPhaseRatio = 0.0;
      }
      if (initObj.hasOwnProperty('footYOffset')) {
        this.footYOffset = initObj.footYOffset
      }
      else {
        this.footYOffset = 0.0;
      }
      if (initObj.hasOwnProperty('riseGain')) {
        this.riseGain = initObj.riseGain
      }
      else {
        this.riseGain = 0.0;
      }
      if (initObj.hasOwnProperty('trunkZOffset')) {
        this.trunkZOffset = initObj.trunkZOffset
      }
      else {
        this.trunkZOffset = 0.0;
      }
      if (initObj.hasOwnProperty('swingGain')) {
        this.swingGain = initObj.swingGain
      }
      else {
        this.swingGain = 0.0;
      }
      if (initObj.hasOwnProperty('swingRollGain')) {
        this.swingRollGain = initObj.swingRollGain
      }
      else {
        this.swingRollGain = 0.0;
      }
      if (initObj.hasOwnProperty('swingPhase')) {
        this.swingPhase = initObj.swingPhase
      }
      else {
        this.swingPhase = 0.0;
      }
      if (initObj.hasOwnProperty('stepUpVel')) {
        this.stepUpVel = initObj.stepUpVel
      }
      else {
        this.stepUpVel = 0.0;
      }
      if (initObj.hasOwnProperty('stepDownVel')) {
        this.stepDownVel = initObj.stepDownVel
      }
      else {
        this.stepDownVel = 0.0;
      }
      if (initObj.hasOwnProperty('riseUpVel')) {
        this.riseUpVel = initObj.riseUpVel
      }
      else {
        this.riseUpVel = 0.0;
      }
      if (initObj.hasOwnProperty('riseDownVel')) {
        this.riseDownVel = initObj.riseDownVel
      }
      else {
        this.riseDownVel = 0.0;
      }
      if (initObj.hasOwnProperty('swingPause')) {
        this.swingPause = initObj.swingPause
      }
      else {
        this.swingPause = 0.0;
      }
      if (initObj.hasOwnProperty('swingVel')) {
        this.swingVel = initObj.swingVel
      }
      else {
        this.swingVel = 0.0;
      }
      if (initObj.hasOwnProperty('trunkXOffset')) {
        this.trunkXOffset = initObj.trunkXOffset
      }
      else {
        this.trunkXOffset = 0.0;
      }
      if (initObj.hasOwnProperty('trunkYOffset')) {
        this.trunkYOffset = initObj.trunkYOffset
      }
      else {
        this.trunkYOffset = 0.0;
      }
      if (initObj.hasOwnProperty('trunkPitch')) {
        this.trunkPitch = initObj.trunkPitch
      }
      else {
        this.trunkPitch = 0.0;
      }
      if (initObj.hasOwnProperty('trunkRoll')) {
        this.trunkRoll = initObj.trunkRoll
      }
      else {
        this.trunkRoll = 0.0;
      }
      if (initObj.hasOwnProperty('extraLeftX')) {
        this.extraLeftX = initObj.extraLeftX
      }
      else {
        this.extraLeftX = 0.0;
      }
      if (initObj.hasOwnProperty('extraLeftY')) {
        this.extraLeftY = initObj.extraLeftY
      }
      else {
        this.extraLeftY = 0.0;
      }
      if (initObj.hasOwnProperty('extraLeftZ')) {
        this.extraLeftZ = initObj.extraLeftZ
      }
      else {
        this.extraLeftZ = 0.0;
      }
      if (initObj.hasOwnProperty('extraRightX')) {
        this.extraRightX = initObj.extraRightX
      }
      else {
        this.extraRightX = 0.0;
      }
      if (initObj.hasOwnProperty('extraRightY')) {
        this.extraRightY = initObj.extraRightY
      }
      else {
        this.extraRightY = 0.0;
      }
      if (initObj.hasOwnProperty('extraRightZ')) {
        this.extraRightZ = initObj.extraRightZ
      }
      else {
        this.extraRightZ = 0.0;
      }
      if (initObj.hasOwnProperty('extraLeftYaw')) {
        this.extraLeftYaw = initObj.extraLeftYaw
      }
      else {
        this.extraLeftYaw = 0.0;
      }
      if (initObj.hasOwnProperty('extraLeftPitch')) {
        this.extraLeftPitch = initObj.extraLeftPitch
      }
      else {
        this.extraLeftPitch = 0.0;
      }
      if (initObj.hasOwnProperty('extraLeftRoll')) {
        this.extraLeftRoll = initObj.extraLeftRoll
      }
      else {
        this.extraLeftRoll = 0.0;
      }
      if (initObj.hasOwnProperty('extraRightYaw')) {
        this.extraRightYaw = initObj.extraRightYaw
      }
      else {
        this.extraRightYaw = 0.0;
      }
      if (initObj.hasOwnProperty('extraRightPitch')) {
        this.extraRightPitch = initObj.extraRightPitch
      }
      else {
        this.extraRightPitch = 0.0;
      }
      if (initObj.hasOwnProperty('extraRightRoll')) {
        this.extraRightRoll = initObj.extraRightRoll
      }
      else {
        this.extraRightRoll = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WalkTestParametersSrvRequest
    // Serialize message field [currentWalk]
    bufferOffset = _serializer.string(obj.currentWalk, buffer, bufferOffset);
    // Serialize message field [stepGain]
    bufferOffset = _serializer.float64(obj.stepGain, buffer, bufferOffset);
    // Serialize message field [lateralGain]
    bufferOffset = _serializer.float64(obj.lateralGain, buffer, bufferOffset);
    // Serialize message field [turnGain]
    bufferOffset = _serializer.float64(obj.turnGain, buffer, bufferOffset);
    // Serialize message field [freq]
    bufferOffset = _serializer.float64(obj.freq, buffer, bufferOffset);
    // Serialize message field [supportPhaseRatio]
    bufferOffset = _serializer.float64(obj.supportPhaseRatio, buffer, bufferOffset);
    // Serialize message field [footYOffset]
    bufferOffset = _serializer.float64(obj.footYOffset, buffer, bufferOffset);
    // Serialize message field [riseGain]
    bufferOffset = _serializer.float64(obj.riseGain, buffer, bufferOffset);
    // Serialize message field [trunkZOffset]
    bufferOffset = _serializer.float64(obj.trunkZOffset, buffer, bufferOffset);
    // Serialize message field [swingGain]
    bufferOffset = _serializer.float64(obj.swingGain, buffer, bufferOffset);
    // Serialize message field [swingRollGain]
    bufferOffset = _serializer.float64(obj.swingRollGain, buffer, bufferOffset);
    // Serialize message field [swingPhase]
    bufferOffset = _serializer.float64(obj.swingPhase, buffer, bufferOffset);
    // Serialize message field [stepUpVel]
    bufferOffset = _serializer.float64(obj.stepUpVel, buffer, bufferOffset);
    // Serialize message field [stepDownVel]
    bufferOffset = _serializer.float64(obj.stepDownVel, buffer, bufferOffset);
    // Serialize message field [riseUpVel]
    bufferOffset = _serializer.float64(obj.riseUpVel, buffer, bufferOffset);
    // Serialize message field [riseDownVel]
    bufferOffset = _serializer.float64(obj.riseDownVel, buffer, bufferOffset);
    // Serialize message field [swingPause]
    bufferOffset = _serializer.float64(obj.swingPause, buffer, bufferOffset);
    // Serialize message field [swingVel]
    bufferOffset = _serializer.float64(obj.swingVel, buffer, bufferOffset);
    // Serialize message field [trunkXOffset]
    bufferOffset = _serializer.float64(obj.trunkXOffset, buffer, bufferOffset);
    // Serialize message field [trunkYOffset]
    bufferOffset = _serializer.float64(obj.trunkYOffset, buffer, bufferOffset);
    // Serialize message field [trunkPitch]
    bufferOffset = _serializer.float64(obj.trunkPitch, buffer, bufferOffset);
    // Serialize message field [trunkRoll]
    bufferOffset = _serializer.float64(obj.trunkRoll, buffer, bufferOffset);
    // Serialize message field [extraLeftX]
    bufferOffset = _serializer.float64(obj.extraLeftX, buffer, bufferOffset);
    // Serialize message field [extraLeftY]
    bufferOffset = _serializer.float64(obj.extraLeftY, buffer, bufferOffset);
    // Serialize message field [extraLeftZ]
    bufferOffset = _serializer.float64(obj.extraLeftZ, buffer, bufferOffset);
    // Serialize message field [extraRightX]
    bufferOffset = _serializer.float64(obj.extraRightX, buffer, bufferOffset);
    // Serialize message field [extraRightY]
    bufferOffset = _serializer.float64(obj.extraRightY, buffer, bufferOffset);
    // Serialize message field [extraRightZ]
    bufferOffset = _serializer.float64(obj.extraRightZ, buffer, bufferOffset);
    // Serialize message field [extraLeftYaw]
    bufferOffset = _serializer.float64(obj.extraLeftYaw, buffer, bufferOffset);
    // Serialize message field [extraLeftPitch]
    bufferOffset = _serializer.float64(obj.extraLeftPitch, buffer, bufferOffset);
    // Serialize message field [extraLeftRoll]
    bufferOffset = _serializer.float64(obj.extraLeftRoll, buffer, bufferOffset);
    // Serialize message field [extraRightYaw]
    bufferOffset = _serializer.float64(obj.extraRightYaw, buffer, bufferOffset);
    // Serialize message field [extraRightPitch]
    bufferOffset = _serializer.float64(obj.extraRightPitch, buffer, bufferOffset);
    // Serialize message field [extraRightRoll]
    bufferOffset = _serializer.float64(obj.extraRightRoll, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WalkTestParametersSrvRequest
    let len;
    let data = new WalkTestParametersSrvRequest(null);
    // Deserialize message field [currentWalk]
    data.currentWalk = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [stepGain]
    data.stepGain = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [lateralGain]
    data.lateralGain = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [turnGain]
    data.turnGain = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [freq]
    data.freq = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [supportPhaseRatio]
    data.supportPhaseRatio = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [footYOffset]
    data.footYOffset = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [riseGain]
    data.riseGain = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trunkZOffset]
    data.trunkZOffset = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [swingGain]
    data.swingGain = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [swingRollGain]
    data.swingRollGain = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [swingPhase]
    data.swingPhase = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [stepUpVel]
    data.stepUpVel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [stepDownVel]
    data.stepDownVel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [riseUpVel]
    data.riseUpVel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [riseDownVel]
    data.riseDownVel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [swingPause]
    data.swingPause = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [swingVel]
    data.swingVel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trunkXOffset]
    data.trunkXOffset = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trunkYOffset]
    data.trunkYOffset = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trunkPitch]
    data.trunkPitch = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trunkRoll]
    data.trunkRoll = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraLeftX]
    data.extraLeftX = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraLeftY]
    data.extraLeftY = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraLeftZ]
    data.extraLeftZ = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraRightX]
    data.extraRightX = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraRightY]
    data.extraRightY = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraRightZ]
    data.extraRightZ = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraLeftYaw]
    data.extraLeftYaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraLeftPitch]
    data.extraLeftPitch = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraLeftRoll]
    data.extraLeftRoll = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraRightYaw]
    data.extraRightYaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraRightPitch]
    data.extraRightPitch = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [extraRightRoll]
    data.extraRightRoll = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.currentWalk);
    return length + 268;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_msgs/WalkTestParametersSrvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '35347b8ea32e09af44278723d78435c9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string currentWalk
    float64 stepGain
    float64 lateralGain
    float64 turnGain
    float64 freq
    float64 supportPhaseRatio
    float64 footYOffset
    float64 riseGain
    float64 trunkZOffset
    float64 swingGain
    float64 swingRollGain
    float64 swingPhase
    float64 stepUpVel
    float64 stepDownVel
    float64 riseUpVel
    float64 riseDownVel
    float64 swingPause
    float64 swingVel
    float64 trunkXOffset
    float64 trunkYOffset
    float64 trunkPitch
    float64 trunkRoll
    float64 extraLeftX
    float64 extraLeftY
    float64 extraLeftZ
    float64 extraRightX
    float64 extraRightY
    float64 extraRightZ
    float64 extraLeftYaw
    float64 extraLeftPitch
    float64 extraLeftRoll
    float64 extraRightYaw
    float64 extraRightPitch
    float64 extraRightRoll
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WalkTestParametersSrvRequest(null);
    if (msg.currentWalk !== undefined) {
      resolved.currentWalk = msg.currentWalk;
    }
    else {
      resolved.currentWalk = ''
    }

    if (msg.stepGain !== undefined) {
      resolved.stepGain = msg.stepGain;
    }
    else {
      resolved.stepGain = 0.0
    }

    if (msg.lateralGain !== undefined) {
      resolved.lateralGain = msg.lateralGain;
    }
    else {
      resolved.lateralGain = 0.0
    }

    if (msg.turnGain !== undefined) {
      resolved.turnGain = msg.turnGain;
    }
    else {
      resolved.turnGain = 0.0
    }

    if (msg.freq !== undefined) {
      resolved.freq = msg.freq;
    }
    else {
      resolved.freq = 0.0
    }

    if (msg.supportPhaseRatio !== undefined) {
      resolved.supportPhaseRatio = msg.supportPhaseRatio;
    }
    else {
      resolved.supportPhaseRatio = 0.0
    }

    if (msg.footYOffset !== undefined) {
      resolved.footYOffset = msg.footYOffset;
    }
    else {
      resolved.footYOffset = 0.0
    }

    if (msg.riseGain !== undefined) {
      resolved.riseGain = msg.riseGain;
    }
    else {
      resolved.riseGain = 0.0
    }

    if (msg.trunkZOffset !== undefined) {
      resolved.trunkZOffset = msg.trunkZOffset;
    }
    else {
      resolved.trunkZOffset = 0.0
    }

    if (msg.swingGain !== undefined) {
      resolved.swingGain = msg.swingGain;
    }
    else {
      resolved.swingGain = 0.0
    }

    if (msg.swingRollGain !== undefined) {
      resolved.swingRollGain = msg.swingRollGain;
    }
    else {
      resolved.swingRollGain = 0.0
    }

    if (msg.swingPhase !== undefined) {
      resolved.swingPhase = msg.swingPhase;
    }
    else {
      resolved.swingPhase = 0.0
    }

    if (msg.stepUpVel !== undefined) {
      resolved.stepUpVel = msg.stepUpVel;
    }
    else {
      resolved.stepUpVel = 0.0
    }

    if (msg.stepDownVel !== undefined) {
      resolved.stepDownVel = msg.stepDownVel;
    }
    else {
      resolved.stepDownVel = 0.0
    }

    if (msg.riseUpVel !== undefined) {
      resolved.riseUpVel = msg.riseUpVel;
    }
    else {
      resolved.riseUpVel = 0.0
    }

    if (msg.riseDownVel !== undefined) {
      resolved.riseDownVel = msg.riseDownVel;
    }
    else {
      resolved.riseDownVel = 0.0
    }

    if (msg.swingPause !== undefined) {
      resolved.swingPause = msg.swingPause;
    }
    else {
      resolved.swingPause = 0.0
    }

    if (msg.swingVel !== undefined) {
      resolved.swingVel = msg.swingVel;
    }
    else {
      resolved.swingVel = 0.0
    }

    if (msg.trunkXOffset !== undefined) {
      resolved.trunkXOffset = msg.trunkXOffset;
    }
    else {
      resolved.trunkXOffset = 0.0
    }

    if (msg.trunkYOffset !== undefined) {
      resolved.trunkYOffset = msg.trunkYOffset;
    }
    else {
      resolved.trunkYOffset = 0.0
    }

    if (msg.trunkPitch !== undefined) {
      resolved.trunkPitch = msg.trunkPitch;
    }
    else {
      resolved.trunkPitch = 0.0
    }

    if (msg.trunkRoll !== undefined) {
      resolved.trunkRoll = msg.trunkRoll;
    }
    else {
      resolved.trunkRoll = 0.0
    }

    if (msg.extraLeftX !== undefined) {
      resolved.extraLeftX = msg.extraLeftX;
    }
    else {
      resolved.extraLeftX = 0.0
    }

    if (msg.extraLeftY !== undefined) {
      resolved.extraLeftY = msg.extraLeftY;
    }
    else {
      resolved.extraLeftY = 0.0
    }

    if (msg.extraLeftZ !== undefined) {
      resolved.extraLeftZ = msg.extraLeftZ;
    }
    else {
      resolved.extraLeftZ = 0.0
    }

    if (msg.extraRightX !== undefined) {
      resolved.extraRightX = msg.extraRightX;
    }
    else {
      resolved.extraRightX = 0.0
    }

    if (msg.extraRightY !== undefined) {
      resolved.extraRightY = msg.extraRightY;
    }
    else {
      resolved.extraRightY = 0.0
    }

    if (msg.extraRightZ !== undefined) {
      resolved.extraRightZ = msg.extraRightZ;
    }
    else {
      resolved.extraRightZ = 0.0
    }

    if (msg.extraLeftYaw !== undefined) {
      resolved.extraLeftYaw = msg.extraLeftYaw;
    }
    else {
      resolved.extraLeftYaw = 0.0
    }

    if (msg.extraLeftPitch !== undefined) {
      resolved.extraLeftPitch = msg.extraLeftPitch;
    }
    else {
      resolved.extraLeftPitch = 0.0
    }

    if (msg.extraLeftRoll !== undefined) {
      resolved.extraLeftRoll = msg.extraLeftRoll;
    }
    else {
      resolved.extraLeftRoll = 0.0
    }

    if (msg.extraRightYaw !== undefined) {
      resolved.extraRightYaw = msg.extraRightYaw;
    }
    else {
      resolved.extraRightYaw = 0.0
    }

    if (msg.extraRightPitch !== undefined) {
      resolved.extraRightPitch = msg.extraRightPitch;
    }
    else {
      resolved.extraRightPitch = 0.0
    }

    if (msg.extraRightRoll !== undefined) {
      resolved.extraRightRoll = msg.extraRightRoll;
    }
    else {
      resolved.extraRightRoll = 0.0
    }

    return resolved;
    }
};

class WalkTestParametersSrvResponse {
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
    // Serializes a message object of type WalkTestParametersSrvResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WalkTestParametersSrvResponse
    let len;
    let data = new WalkTestParametersSrvResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'movement_msgs/WalkTestParametersSrvResponse';
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
    const resolved = new WalkTestParametersSrvResponse(null);
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
  Request: WalkTestParametersSrvRequest,
  Response: WalkTestParametersSrvResponse,
  md5sum() { return '7113a794fe0bdf7ad1da5428852cd6a2'; },
  datatype() { return 'movement_msgs/WalkTestParametersSrv'; }
};
