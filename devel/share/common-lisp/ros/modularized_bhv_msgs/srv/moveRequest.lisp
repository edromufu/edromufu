; Auto-generated. Do not edit!


(cl:in-package modularized_bhv_msgs-srv)


;//! \htmlinclude moveRequest-request.msg.html

(cl:defclass <moveRequest-request> (roslisp-msg-protocol:ros-message)
  ((moveRequest
    :reader moveRequest
    :initarg :moveRequest
    :type cl:string
    :initform ""))
)

(cl:defclass moveRequest-request (<moveRequest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <moveRequest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'moveRequest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name modularized_bhv_msgs-srv:<moveRequest-request> is deprecated: use modularized_bhv_msgs-srv:moveRequest-request instead.")))

(cl:ensure-generic-function 'moveRequest-val :lambda-list '(m))
(cl:defmethod moveRequest-val ((m <moveRequest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-srv:moveRequest-val is deprecated.  Use modularized_bhv_msgs-srv:moveRequest instead.")
  (moveRequest m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <moveRequest-request>) ostream)
  "Serializes a message object of type '<moveRequest-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'moveRequest))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'moveRequest))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <moveRequest-request>) istream)
  "Deserializes a message object of type '<moveRequest-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'moveRequest) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'moveRequest) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<moveRequest-request>)))
  "Returns string type for a service object of type '<moveRequest-request>"
  "modularized_bhv_msgs/moveRequestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'moveRequest-request)))
  "Returns string type for a service object of type 'moveRequest-request"
  "modularized_bhv_msgs/moveRequestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<moveRequest-request>)))
  "Returns md5sum for a message object of type '<moveRequest-request>"
  "fa4c3676b8fc489dd65422b45b94f727")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'moveRequest-request)))
  "Returns md5sum for a message object of type 'moveRequest-request"
  "fa4c3676b8fc489dd65422b45b94f727")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<moveRequest-request>)))
  "Returns full string definition for message of type '<moveRequest-request>"
  (cl:format cl:nil "string moveRequest~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'moveRequest-request)))
  "Returns full string definition for message of type 'moveRequest-request"
  (cl:format cl:nil "string moveRequest~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <moveRequest-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'moveRequest))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <moveRequest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'moveRequest-request
    (cl:cons ':moveRequest (moveRequest msg))
))
;//! \htmlinclude moveRequest-response.msg.html

(cl:defclass <moveRequest-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass moveRequest-response (<moveRequest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <moveRequest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'moveRequest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name modularized_bhv_msgs-srv:<moveRequest-response> is deprecated: use modularized_bhv_msgs-srv:moveRequest-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <moveRequest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader modularized_bhv_msgs-srv:success-val is deprecated.  Use modularized_bhv_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <moveRequest-response>) ostream)
  "Serializes a message object of type '<moveRequest-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <moveRequest-response>) istream)
  "Deserializes a message object of type '<moveRequest-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<moveRequest-response>)))
  "Returns string type for a service object of type '<moveRequest-response>"
  "modularized_bhv_msgs/moveRequestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'moveRequest-response)))
  "Returns string type for a service object of type 'moveRequest-response"
  "modularized_bhv_msgs/moveRequestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<moveRequest-response>)))
  "Returns md5sum for a message object of type '<moveRequest-response>"
  "fa4c3676b8fc489dd65422b45b94f727")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'moveRequest-response)))
  "Returns md5sum for a message object of type 'moveRequest-response"
  "fa4c3676b8fc489dd65422b45b94f727")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<moveRequest-response>)))
  "Returns full string definition for message of type '<moveRequest-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'moveRequest-response)))
  "Returns full string definition for message of type 'moveRequest-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <moveRequest-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <moveRequest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'moveRequest-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'moveRequest)))
  'moveRequest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'moveRequest)))
  'moveRequest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'moveRequest)))
  "Returns string type for a service object of type '<moveRequest>"
  "modularized_bhv_msgs/moveRequest")