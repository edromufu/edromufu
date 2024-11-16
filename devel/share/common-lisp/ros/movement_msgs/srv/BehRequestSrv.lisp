; Auto-generated. Do not edit!


(cl:in-package movement_msgs-srv)


;//! \htmlinclude BehRequestSrv-request.msg.html

(cl:defclass <BehRequestSrv-request> (roslisp-msg-protocol:ros-message)
  ((required_movement
    :reader required_movement
    :initarg :required_movement
    :type cl:string
    :initform "")
   (required_status
    :reader required_status
    :initarg :required_status
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass BehRequestSrv-request (<BehRequestSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BehRequestSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BehRequestSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-srv:<BehRequestSrv-request> is deprecated: use movement_msgs-srv:BehRequestSrv-request instead.")))

(cl:ensure-generic-function 'required_movement-val :lambda-list '(m))
(cl:defmethod required_movement-val ((m <BehRequestSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-srv:required_movement-val is deprecated.  Use movement_msgs-srv:required_movement instead.")
  (required_movement m))

(cl:ensure-generic-function 'required_status-val :lambda-list '(m))
(cl:defmethod required_status-val ((m <BehRequestSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-srv:required_status-val is deprecated.  Use movement_msgs-srv:required_status instead.")
  (required_status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BehRequestSrv-request>) ostream)
  "Serializes a message object of type '<BehRequestSrv-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'required_movement))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'required_movement))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'required_status) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BehRequestSrv-request>) istream)
  "Deserializes a message object of type '<BehRequestSrv-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'required_movement) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'required_movement) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'required_status) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BehRequestSrv-request>)))
  "Returns string type for a service object of type '<BehRequestSrv-request>"
  "movement_msgs/BehRequestSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BehRequestSrv-request)))
  "Returns string type for a service object of type 'BehRequestSrv-request"
  "movement_msgs/BehRequestSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BehRequestSrv-request>)))
  "Returns md5sum for a message object of type '<BehRequestSrv-request>"
  "4f5d36d25e04a31db12adbc950d9b1a5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BehRequestSrv-request)))
  "Returns md5sum for a message object of type 'BehRequestSrv-request"
  "4f5d36d25e04a31db12adbc950d9b1a5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BehRequestSrv-request>)))
  "Returns full string definition for message of type '<BehRequestSrv-request>"
  (cl:format cl:nil "string required_movement~%bool required_status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BehRequestSrv-request)))
  "Returns full string definition for message of type 'BehRequestSrv-request"
  (cl:format cl:nil "string required_movement~%bool required_status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BehRequestSrv-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'required_movement))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BehRequestSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BehRequestSrv-request
    (cl:cons ':required_movement (required_movement msg))
    (cl:cons ':required_status (required_status msg))
))
;//! \htmlinclude BehRequestSrv-response.msg.html

(cl:defclass <BehRequestSrv-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass BehRequestSrv-response (<BehRequestSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BehRequestSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BehRequestSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-srv:<BehRequestSrv-response> is deprecated: use movement_msgs-srv:BehRequestSrv-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <BehRequestSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-srv:response-val is deprecated.  Use movement_msgs-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BehRequestSrv-response>) ostream)
  "Serializes a message object of type '<BehRequestSrv-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'response) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BehRequestSrv-response>) istream)
  "Deserializes a message object of type '<BehRequestSrv-response>"
    (cl:setf (cl:slot-value msg 'response) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BehRequestSrv-response>)))
  "Returns string type for a service object of type '<BehRequestSrv-response>"
  "movement_msgs/BehRequestSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BehRequestSrv-response)))
  "Returns string type for a service object of type 'BehRequestSrv-response"
  "movement_msgs/BehRequestSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BehRequestSrv-response>)))
  "Returns md5sum for a message object of type '<BehRequestSrv-response>"
  "4f5d36d25e04a31db12adbc950d9b1a5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BehRequestSrv-response)))
  "Returns md5sum for a message object of type 'BehRequestSrv-response"
  "4f5d36d25e04a31db12adbc950d9b1a5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BehRequestSrv-response>)))
  "Returns full string definition for message of type '<BehRequestSrv-response>"
  (cl:format cl:nil "~%bool response~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BehRequestSrv-response)))
  "Returns full string definition for message of type 'BehRequestSrv-response"
  (cl:format cl:nil "~%bool response~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BehRequestSrv-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BehRequestSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BehRequestSrv-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BehRequestSrv)))
  'BehRequestSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BehRequestSrv)))
  'BehRequestSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BehRequestSrv)))
  "Returns string type for a service object of type '<BehRequestSrv>"
  "movement_msgs/BehRequestSrv")