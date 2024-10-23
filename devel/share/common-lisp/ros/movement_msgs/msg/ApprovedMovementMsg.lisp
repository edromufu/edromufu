; Auto-generated. Do not edit!


(cl:in-package movement_msgs-msg)


;//! \htmlinclude ApprovedMovementMsg.msg.html

(cl:defclass <ApprovedMovementMsg> (roslisp-msg-protocol:ros-message)
  ((approved_movement
    :reader approved_movement
    :initarg :approved_movement
    :type cl:string
    :initform ""))
)

(cl:defclass ApprovedMovementMsg (<ApprovedMovementMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ApprovedMovementMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ApprovedMovementMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-msg:<ApprovedMovementMsg> is deprecated: use movement_msgs-msg:ApprovedMovementMsg instead.")))

(cl:ensure-generic-function 'approved_movement-val :lambda-list '(m))
(cl:defmethod approved_movement-val ((m <ApprovedMovementMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:approved_movement-val is deprecated.  Use movement_msgs-msg:approved_movement instead.")
  (approved_movement m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ApprovedMovementMsg>) ostream)
  "Serializes a message object of type '<ApprovedMovementMsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'approved_movement))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'approved_movement))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ApprovedMovementMsg>) istream)
  "Deserializes a message object of type '<ApprovedMovementMsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'approved_movement) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'approved_movement) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ApprovedMovementMsg>)))
  "Returns string type for a message object of type '<ApprovedMovementMsg>"
  "movement_msgs/ApprovedMovementMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ApprovedMovementMsg)))
  "Returns string type for a message object of type 'ApprovedMovementMsg"
  "movement_msgs/ApprovedMovementMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ApprovedMovementMsg>)))
  "Returns md5sum for a message object of type '<ApprovedMovementMsg>"
  "255fbce3bb4374d8b5382cbf8e9f1840")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ApprovedMovementMsg)))
  "Returns md5sum for a message object of type 'ApprovedMovementMsg"
  "255fbce3bb4374d8b5382cbf8e9f1840")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ApprovedMovementMsg>)))
  "Returns full string definition for message of type '<ApprovedMovementMsg>"
  (cl:format cl:nil "string approved_movement~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ApprovedMovementMsg)))
  "Returns full string definition for message of type 'ApprovedMovementMsg"
  (cl:format cl:nil "string approved_movement~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ApprovedMovementMsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'approved_movement))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ApprovedMovementMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'ApprovedMovementMsg
    (cl:cons ':approved_movement (approved_movement msg))
))
