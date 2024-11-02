; Auto-generated. Do not edit!


(cl:in-package movement_msgs-msg)


;//! \htmlinclude WebotsRequestMsg.msg.html

(cl:defclass <WebotsRequestMsg> (roslisp-msg-protocol:ros-message)
  ((motors_position
    :reader motors_position
    :initarg :motors_position
    :type (cl:vector cl:float)
   :initform (cl:make-array 20 :element-type 'cl:float :initial-element 0.0))
   (motors_velocity
    :reader motors_velocity
    :initarg :motors_velocity
    :type (cl:vector cl:float)
   :initform (cl:make-array 20 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass WebotsRequestMsg (<WebotsRequestMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WebotsRequestMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WebotsRequestMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-msg:<WebotsRequestMsg> is deprecated: use movement_msgs-msg:WebotsRequestMsg instead.")))

(cl:ensure-generic-function 'motors_position-val :lambda-list '(m))
(cl:defmethod motors_position-val ((m <WebotsRequestMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:motors_position-val is deprecated.  Use movement_msgs-msg:motors_position instead.")
  (motors_position m))

(cl:ensure-generic-function 'motors_velocity-val :lambda-list '(m))
(cl:defmethod motors_velocity-val ((m <WebotsRequestMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:motors_velocity-val is deprecated.  Use movement_msgs-msg:motors_velocity instead.")
  (motors_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WebotsRequestMsg>) ostream)
  "Serializes a message object of type '<WebotsRequestMsg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'motors_position))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'motors_velocity))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WebotsRequestMsg>) istream)
  "Deserializes a message object of type '<WebotsRequestMsg>"
  (cl:setf (cl:slot-value msg 'motors_position) (cl:make-array 20))
  (cl:let ((vals (cl:slot-value msg 'motors_position)))
    (cl:dotimes (i 20)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  (cl:setf (cl:slot-value msg 'motors_velocity) (cl:make-array 20))
  (cl:let ((vals (cl:slot-value msg 'motors_velocity)))
    (cl:dotimes (i 20)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WebotsRequestMsg>)))
  "Returns string type for a message object of type '<WebotsRequestMsg>"
  "movement_msgs/WebotsRequestMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WebotsRequestMsg)))
  "Returns string type for a message object of type 'WebotsRequestMsg"
  "movement_msgs/WebotsRequestMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WebotsRequestMsg>)))
  "Returns md5sum for a message object of type '<WebotsRequestMsg>"
  "3463d5e3ddb49315fab6bfa4cde9cb44")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WebotsRequestMsg)))
  "Returns md5sum for a message object of type 'WebotsRequestMsg"
  "3463d5e3ddb49315fab6bfa4cde9cb44")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WebotsRequestMsg>)))
  "Returns full string definition for message of type '<WebotsRequestMsg>"
  (cl:format cl:nil "float32[20] motors_position~%float32[20] motors_velocity~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WebotsRequestMsg)))
  "Returns full string definition for message of type 'WebotsRequestMsg"
  (cl:format cl:nil "float32[20] motors_position~%float32[20] motors_velocity~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WebotsRequestMsg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'motors_position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'motors_velocity) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WebotsRequestMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'WebotsRequestMsg
    (cl:cons ':motors_position (motors_position msg))
    (cl:cons ':motors_velocity (motors_velocity msg))
))
