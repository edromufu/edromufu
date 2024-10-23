; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude page-request.msg.html

(cl:defclass <page-request> (roslisp-msg-protocol:ros-message)
  ((page_name
    :reader page_name
    :initarg :page_name
    :type cl:string
    :initform ""))
)

(cl:defclass page-request (<page-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <page-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'page-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<page-request> is deprecated: use movement_utils-srv:page-request instead.")))

(cl:ensure-generic-function 'page_name-val :lambda-list '(m))
(cl:defmethod page_name-val ((m <page-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:page_name-val is deprecated.  Use movement_utils-srv:page_name instead.")
  (page_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <page-request>) ostream)
  "Serializes a message object of type '<page-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'page_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'page_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <page-request>) istream)
  "Deserializes a message object of type '<page-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'page_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'page_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<page-request>)))
  "Returns string type for a service object of type '<page-request>"
  "movement_utils/pageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'page-request)))
  "Returns string type for a service object of type 'page-request"
  "movement_utils/pageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<page-request>)))
  "Returns md5sum for a message object of type '<page-request>"
  "4f331e5d3a60dd4df8ef3fcaed28acb9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'page-request)))
  "Returns md5sum for a message object of type 'page-request"
  "4f331e5d3a60dd4df8ef3fcaed28acb9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<page-request>)))
  "Returns full string definition for message of type '<page-request>"
  (cl:format cl:nil "string page_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'page-request)))
  "Returns full string definition for message of type 'page-request"
  (cl:format cl:nil "string page_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <page-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'page_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <page-request>))
  "Converts a ROS message object to a list"
  (cl:list 'page-request
    (cl:cons ':page_name (page_name msg))
))
;//! \htmlinclude page-response.msg.html

(cl:defclass <page-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass page-response (<page-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <page-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'page-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<page-response> is deprecated: use movement_utils-srv:page-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <page-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <page-response>) ostream)
  "Serializes a message object of type '<page-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <page-response>) istream)
  "Deserializes a message object of type '<page-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<page-response>)))
  "Returns string type for a service object of type '<page-response>"
  "movement_utils/pageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'page-response)))
  "Returns string type for a service object of type 'page-response"
  "movement_utils/pageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<page-response>)))
  "Returns md5sum for a message object of type '<page-response>"
  "4f331e5d3a60dd4df8ef3fcaed28acb9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'page-response)))
  "Returns md5sum for a message object of type 'page-response"
  "4f331e5d3a60dd4df8ef3fcaed28acb9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<page-response>)))
  "Returns full string definition for message of type '<page-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'page-response)))
  "Returns full string definition for message of type 'page-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <page-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <page-response>))
  "Converts a ROS message object to a list"
  (cl:list 'page-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'page)))
  'page-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'page)))
  'page-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'page)))
  "Returns string type for a service object of type '<page>"
  "movement_utils/page")