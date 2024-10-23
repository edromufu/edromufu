; Auto-generated. Do not edit!


(cl:in-package modularized_bhv_msgs-msg)


;//! \htmlinclude currentStateMsg.msg.html

(cl:defclass <currentStateMsg> (roslisp-msg-protocol:ros-message)
  ((currentState
    :reader currentState
    :initarg :currentState
    :type cl:string
    :initform ""))
)

(cl:defclass currentStateMsg (<currentStateMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <currentStateMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'currentStateMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name modularized_bhv_msgs-msg:<currentStateMsg> is deprecated: use modularized_bhv_msgs-msg:currentStateMsg instead.")))

(cl:ensure-generic-function 'currentState-val :lambda-list '(m))
(cl:defmethod currentState-val ((m <currentStateMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-msg:currentState-val is deprecated.  Use modularized_bhv_msgs-msg:currentState instead.")
  (currentState m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <currentStateMsg>) ostream)
  "Serializes a message object of type '<currentStateMsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'currentState))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'currentState))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <currentStateMsg>) istream)
  "Deserializes a message object of type '<currentStateMsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'currentState) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'currentState) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<currentStateMsg>)))
  "Returns string type for a message object of type '<currentStateMsg>"
  "modularized_bhv_msgs/currentStateMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'currentStateMsg)))
  "Returns string type for a message object of type 'currentStateMsg"
  "modularized_bhv_msgs/currentStateMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<currentStateMsg>)))
  "Returns md5sum for a message object of type '<currentStateMsg>"
  "51b88f6d6df0913c6465fdbbb69a8c4e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'currentStateMsg)))
  "Returns md5sum for a message object of type 'currentStateMsg"
  "51b88f6d6df0913c6465fdbbb69a8c4e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<currentStateMsg>)))
  "Returns full string definition for message of type '<currentStateMsg>"
  (cl:format cl:nil "string currentState~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'currentStateMsg)))
  "Returns full string definition for message of type 'currentStateMsg"
  (cl:format cl:nil "string currentState~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <currentStateMsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'currentState))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <currentStateMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'currentStateMsg
    (cl:cons ':currentState (currentState msg))
))
