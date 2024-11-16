; Auto-generated. Do not edit!


(cl:in-package movement_msgs-msg)


;//! \htmlinclude WalkCreatorRequestMsg.msg.html

(cl:defclass <WalkCreatorRequestMsg> (roslisp-msg-protocol:ros-message)
  ((enabledGain
    :reader enabledGain
    :initarg :enabledGain
    :type cl:boolean
    :initform cl:nil)
   (stepGain
    :reader stepGain
    :initarg :stepGain
    :type cl:float
    :initform 0.0)
   (lateralGain
    :reader lateralGain
    :initarg :lateralGain
    :type cl:float
    :initform 0.0)
   (turnGain
    :reader turnGain
    :initarg :turnGain
    :type cl:float
    :initform 0.0))
)

(cl:defclass WalkCreatorRequestMsg (<WalkCreatorRequestMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WalkCreatorRequestMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WalkCreatorRequestMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-msg:<WalkCreatorRequestMsg> is deprecated: use movement_msgs-msg:WalkCreatorRequestMsg instead.")))

(cl:ensure-generic-function 'enabledGain-val :lambda-list '(m))
(cl:defmethod enabledGain-val ((m <WalkCreatorRequestMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:enabledGain-val is deprecated.  Use movement_msgs-msg:enabledGain instead.")
  (enabledGain m))

(cl:ensure-generic-function 'stepGain-val :lambda-list '(m))
(cl:defmethod stepGain-val ((m <WalkCreatorRequestMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:stepGain-val is deprecated.  Use movement_msgs-msg:stepGain instead.")
  (stepGain m))

(cl:ensure-generic-function 'lateralGain-val :lambda-list '(m))
(cl:defmethod lateralGain-val ((m <WalkCreatorRequestMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:lateralGain-val is deprecated.  Use movement_msgs-msg:lateralGain instead.")
  (lateralGain m))

(cl:ensure-generic-function 'turnGain-val :lambda-list '(m))
(cl:defmethod turnGain-val ((m <WalkCreatorRequestMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:turnGain-val is deprecated.  Use movement_msgs-msg:turnGain instead.")
  (turnGain m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WalkCreatorRequestMsg>) ostream)
  "Serializes a message object of type '<WalkCreatorRequestMsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enabledGain) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'stepGain))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lateralGain))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'turnGain))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WalkCreatorRequestMsg>) istream)
  "Deserializes a message object of type '<WalkCreatorRequestMsg>"
    (cl:setf (cl:slot-value msg 'enabledGain) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'stepGain) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lateralGain) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'turnGain) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WalkCreatorRequestMsg>)))
  "Returns string type for a message object of type '<WalkCreatorRequestMsg>"
  "movement_msgs/WalkCreatorRequestMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WalkCreatorRequestMsg)))
  "Returns string type for a message object of type 'WalkCreatorRequestMsg"
  "movement_msgs/WalkCreatorRequestMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WalkCreatorRequestMsg>)))
  "Returns md5sum for a message object of type '<WalkCreatorRequestMsg>"
  "9b4b735c8495180479cdcb415b06f8d4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WalkCreatorRequestMsg)))
  "Returns md5sum for a message object of type 'WalkCreatorRequestMsg"
  "9b4b735c8495180479cdcb415b06f8d4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WalkCreatorRequestMsg>)))
  "Returns full string definition for message of type '<WalkCreatorRequestMsg>"
  (cl:format cl:nil "bool   enabledGain~%float32 stepGain~%float32 lateralGain~%float32 turnGain~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WalkCreatorRequestMsg)))
  "Returns full string definition for message of type 'WalkCreatorRequestMsg"
  (cl:format cl:nil "bool   enabledGain~%float32 stepGain~%float32 lateralGain~%float32 turnGain~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WalkCreatorRequestMsg>))
  (cl:+ 0
     1
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WalkCreatorRequestMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'WalkCreatorRequestMsg
    (cl:cons ':enabledGain (enabledGain msg))
    (cl:cons ':stepGain (stepGain msg))
    (cl:cons ':lateralGain (lateralGain msg))
    (cl:cons ':turnGain (turnGain msg))
))
