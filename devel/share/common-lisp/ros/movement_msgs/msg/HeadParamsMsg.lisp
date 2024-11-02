; Auto-generated. Do not edit!


(cl:in-package movement_msgs-msg)


;//! \htmlinclude HeadParamsMsg.msg.html

(cl:defclass <HeadParamsMsg> (roslisp-msg-protocol:ros-message)
  ((direction
    :reader direction
    :initarg :direction
    :type cl:string
    :initform "")
   (pattern
    :reader pattern
    :initarg :pattern
    :type cl:string
    :initform ""))
)

(cl:defclass HeadParamsMsg (<HeadParamsMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HeadParamsMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HeadParamsMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-msg:<HeadParamsMsg> is deprecated: use movement_msgs-msg:HeadParamsMsg instead.")))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <HeadParamsMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:direction-val is deprecated.  Use movement_msgs-msg:direction instead.")
  (direction m))

(cl:ensure-generic-function 'pattern-val :lambda-list '(m))
(cl:defmethod pattern-val ((m <HeadParamsMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:pattern-val is deprecated.  Use movement_msgs-msg:pattern instead.")
  (pattern m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HeadParamsMsg>) ostream)
  "Serializes a message object of type '<HeadParamsMsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'direction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'direction))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'pattern))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'pattern))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HeadParamsMsg>) istream)
  "Deserializes a message object of type '<HeadParamsMsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'direction) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'direction) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pattern) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'pattern) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HeadParamsMsg>)))
  "Returns string type for a message object of type '<HeadParamsMsg>"
  "movement_msgs/HeadParamsMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HeadParamsMsg)))
  "Returns string type for a message object of type 'HeadParamsMsg"
  "movement_msgs/HeadParamsMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HeadParamsMsg>)))
  "Returns md5sum for a message object of type '<HeadParamsMsg>"
  "bd8add9ae07028e68b98196268fea8b1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HeadParamsMsg)))
  "Returns md5sum for a message object of type 'HeadParamsMsg"
  "bd8add9ae07028e68b98196268fea8b1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HeadParamsMsg>)))
  "Returns full string definition for message of type '<HeadParamsMsg>"
  (cl:format cl:nil "string direction~%string pattern~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HeadParamsMsg)))
  "Returns full string definition for message of type 'HeadParamsMsg"
  (cl:format cl:nil "string direction~%string pattern~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HeadParamsMsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'direction))
     4 (cl:length (cl:slot-value msg 'pattern))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HeadParamsMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'HeadParamsMsg
    (cl:cons ':direction (direction msg))
    (cl:cons ':pattern (pattern msg))
))
