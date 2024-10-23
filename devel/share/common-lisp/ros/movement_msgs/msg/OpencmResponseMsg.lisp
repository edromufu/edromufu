; Auto-generated. Do not edit!


(cl:in-package movement_msgs-msg)


;//! \htmlinclude OpencmResponseMsg.msg.html

(cl:defclass <OpencmResponseMsg> (roslisp-msg-protocol:ros-message)
  ((motors_position
    :reader motors_position
    :initarg :motors_position
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 20 :element-type 'cl:fixnum :initial-element 0))
   (motors_velocity
    :reader motors_velocity
    :initarg :motors_velocity
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 20 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass OpencmResponseMsg (<OpencmResponseMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OpencmResponseMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OpencmResponseMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-msg:<OpencmResponseMsg> is deprecated: use movement_msgs-msg:OpencmResponseMsg instead.")))

(cl:ensure-generic-function 'motors_position-val :lambda-list '(m))
(cl:defmethod motors_position-val ((m <OpencmResponseMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:motors_position-val is deprecated.  Use movement_msgs-msg:motors_position instead.")
  (motors_position m))

(cl:ensure-generic-function 'motors_velocity-val :lambda-list '(m))
(cl:defmethod motors_velocity-val ((m <OpencmResponseMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:motors_velocity-val is deprecated.  Use movement_msgs-msg:motors_velocity instead.")
  (motors_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OpencmResponseMsg>) ostream)
  "Serializes a message object of type '<OpencmResponseMsg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'motors_position))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'motors_velocity))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OpencmResponseMsg>) istream)
  "Deserializes a message object of type '<OpencmResponseMsg>"
  (cl:setf (cl:slot-value msg 'motors_position) (cl:make-array 20))
  (cl:let ((vals (cl:slot-value msg 'motors_position)))
    (cl:dotimes (i 20)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  (cl:setf (cl:slot-value msg 'motors_velocity) (cl:make-array 20))
  (cl:let ((vals (cl:slot-value msg 'motors_velocity)))
    (cl:dotimes (i 20)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OpencmResponseMsg>)))
  "Returns string type for a message object of type '<OpencmResponseMsg>"
  "movement_msgs/OpencmResponseMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OpencmResponseMsg)))
  "Returns string type for a message object of type 'OpencmResponseMsg"
  "movement_msgs/OpencmResponseMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OpencmResponseMsg>)))
  "Returns md5sum for a message object of type '<OpencmResponseMsg>"
  "f292bdc80699153415d4562d7f08a5e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OpencmResponseMsg)))
  "Returns md5sum for a message object of type 'OpencmResponseMsg"
  "f292bdc80699153415d4562d7f08a5e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OpencmResponseMsg>)))
  "Returns full string definition for message of type '<OpencmResponseMsg>"
  (cl:format cl:nil "int16[20] motors_position~%int16[20] motors_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OpencmResponseMsg)))
  "Returns full string definition for message of type 'OpencmResponseMsg"
  (cl:format cl:nil "int16[20] motors_position~%int16[20] motors_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OpencmResponseMsg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'motors_position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'motors_velocity) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OpencmResponseMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'OpencmResponseMsg
    (cl:cons ':motors_position (motors_position msg))
    (cl:cons ':motors_velocity (motors_velocity msg))
))
