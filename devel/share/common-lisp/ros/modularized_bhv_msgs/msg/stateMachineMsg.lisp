; Auto-generated. Do not edit!


(cl:in-package modularized_bhv_msgs-msg)


;//! \htmlinclude stateMachineMsg.msg.html

(cl:defclass <stateMachineMsg> (roslisp-msg-protocol:ros-message)
  ((ballPosition
    :reader ballPosition
    :initarg :ballPosition
    :type cl:string
    :initform "")
   (ballClose
    :reader ballClose
    :initarg :ballClose
    :type cl:boolean
    :initform cl:nil)
   (ballFound
    :reader ballFound
    :initarg :ballFound
    :type cl:boolean
    :initform cl:nil)
   (fallState
    :reader fallState
    :initarg :fallState
    :type cl:string
    :initform "")
   (horMotorOutOfCenter
    :reader horMotorOutOfCenter
    :initarg :horMotorOutOfCenter
    :type cl:string
    :initform "")
   (headKickCheck
    :reader headKickCheck
    :initarg :headKickCheck
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass stateMachineMsg (<stateMachineMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <stateMachineMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'stateMachineMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name modularized_bhv_msgs-msg:<stateMachineMsg> is deprecated: use modularized_bhv_msgs-msg:stateMachineMsg instead.")))

(cl:ensure-generic-function 'ballPosition-val :lambda-list '(m))
(cl:defmethod ballPosition-val ((m <stateMachineMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:ballPosition-val is deprecated.  Use modularized_bhv_msgs-msg:ballPosition instead.")
  (ballPosition m))

(cl:ensure-generic-function 'ballClose-val :lambda-list '(m))
(cl:defmethod ballClose-val ((m <stateMachineMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:ballClose-val is deprecated.  Use modularized_bhv_msgs-msg:ballClose instead.")
  (ballClose m))

(cl:ensure-generic-function 'ballFound-val :lambda-list '(m))
(cl:defmethod ballFound-val ((m <stateMachineMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:ballFound-val is deprecated.  Use modularized_bhv_msgs-msg:ballFound instead.")
  (ballFound m))

(cl:ensure-generic-function 'fallState-val :lambda-list '(m))
(cl:defmethod fallState-val ((m <stateMachineMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:fallState-val is deprecated.  Use modularized_bhv_msgs-msg:fallState instead.")
  (fallState m))

(cl:ensure-generic-function 'horMotorOutOfCenter-val :lambda-list '(m))
(cl:defmethod horMotorOutOfCenter-val ((m <stateMachineMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:horMotorOutOfCenter-val is deprecated.  Use modularized_bhv_msgs-msg:horMotorOutOfCenter instead.")
  (horMotorOutOfCenter m))

(cl:ensure-generic-function 'headKickCheck-val :lambda-list '(m))
(cl:defmethod headKickCheck-val ((m <stateMachineMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:headKickCheck-val is deprecated.  Use modularized_bhv_msgs-msg:headKickCheck instead.")
  (headKickCheck m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <stateMachineMsg>) ostream)
  "Serializes a message object of type '<stateMachineMsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'ballPosition))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'ballPosition))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ballClose) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ballFound) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'fallState))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'fallState))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'horMotorOutOfCenter))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'horMotorOutOfCenter))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'headKickCheck) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <stateMachineMsg>) istream)
  "Deserializes a message object of type '<stateMachineMsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ballPosition) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'ballPosition) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'ballClose) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'ballFound) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fallState) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'fallState) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'horMotorOutOfCenter) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'horMotorOutOfCenter) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'headKickCheck) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<stateMachineMsg>)))
  "Returns string type for a message object of type '<stateMachineMsg>"
  "modularized_bhv_msgs/stateMachineMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'stateMachineMsg)))
  "Returns string type for a message object of type 'stateMachineMsg"
  "modularized_bhv_msgs/stateMachineMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<stateMachineMsg>)))
  "Returns md5sum for a message object of type '<stateMachineMsg>"
  "c591d7d3c44206a23a253ed3e26e96da")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'stateMachineMsg)))
  "Returns md5sum for a message object of type 'stateMachineMsg"
  "c591d7d3c44206a23a253ed3e26e96da")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<stateMachineMsg>)))
  "Returns full string definition for message of type '<stateMachineMsg>"
  (cl:format cl:nil "string ballPosition~%bool ballClose~%bool ballFound~%string fallState~%string horMotorOutOfCenter~%bool headKickCheck~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'stateMachineMsg)))
  "Returns full string definition for message of type 'stateMachineMsg"
  (cl:format cl:nil "string ballPosition~%bool ballClose~%bool ballFound~%string fallState~%string horMotorOutOfCenter~%bool headKickCheck~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <stateMachineMsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'ballPosition))
     1
     1
     4 (cl:length (cl:slot-value msg 'fallState))
     4 (cl:length (cl:slot-value msg 'horMotorOutOfCenter))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <stateMachineMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'stateMachineMsg
    (cl:cons ':ballPosition (ballPosition msg))
    (cl:cons ':ballClose (ballClose msg))
    (cl:cons ':ballFound (ballFound msg))
    (cl:cons ':fallState (fallState msg))
    (cl:cons ':horMotorOutOfCenter (horMotorOutOfCenter msg))
    (cl:cons ':headKickCheck (headKickCheck msg))
))
