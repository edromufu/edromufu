; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude balance-request.msg.html

(cl:defclass <balance-request> (roslisp-msg-protocol:ros-message)
  ((supported_foot
    :reader supported_foot
    :initarg :supported_foot
    :type cl:fixnum
    :initform 0))
)

(cl:defclass balance-request (<balance-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <balance-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'balance-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<balance-request> is deprecated: use movement_utils-srv:balance-request instead.")))

(cl:ensure-generic-function 'supported_foot-val :lambda-list '(m))
(cl:defmethod supported_foot-val ((m <balance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:supported_foot-val is deprecated.  Use movement_utils-srv:supported_foot instead.")
  (supported_foot m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <balance-request>) ostream)
  "Serializes a message object of type '<balance-request>"
  (cl:let* ((signed (cl:slot-value msg 'supported_foot)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <balance-request>) istream)
  "Deserializes a message object of type '<balance-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'supported_foot) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<balance-request>)))
  "Returns string type for a service object of type '<balance-request>"
  "movement_utils/balanceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'balance-request)))
  "Returns string type for a service object of type 'balance-request"
  "movement_utils/balanceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<balance-request>)))
  "Returns md5sum for a message object of type '<balance-request>"
  "01c548ad4bcd6f9d88f95b8adc185129")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'balance-request)))
  "Returns md5sum for a message object of type 'balance-request"
  "01c548ad4bcd6f9d88f95b8adc185129")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<balance-request>)))
  "Returns full string definition for message of type '<balance-request>"
  (cl:format cl:nil "int8 supported_foot~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'balance-request)))
  "Returns full string definition for message of type 'balance-request"
  (cl:format cl:nil "int8 supported_foot~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <balance-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <balance-request>))
  "Converts a ROS message object to a list"
  (cl:list 'balance-request
    (cl:cons ':supported_foot (supported_foot msg))
))
;//! \htmlinclude balance-response.msg.html

(cl:defclass <balance-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass balance-response (<balance-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <balance-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'balance-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<balance-response> is deprecated: use movement_utils-srv:balance-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <balance-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <balance-response>) ostream)
  "Serializes a message object of type '<balance-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <balance-response>) istream)
  "Deserializes a message object of type '<balance-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<balance-response>)))
  "Returns string type for a service object of type '<balance-response>"
  "movement_utils/balanceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'balance-response)))
  "Returns string type for a service object of type 'balance-response"
  "movement_utils/balanceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<balance-response>)))
  "Returns md5sum for a message object of type '<balance-response>"
  "01c548ad4bcd6f9d88f95b8adc185129")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'balance-response)))
  "Returns md5sum for a message object of type 'balance-response"
  "01c548ad4bcd6f9d88f95b8adc185129")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<balance-response>)))
  "Returns full string definition for message of type '<balance-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'balance-response)))
  "Returns full string definition for message of type 'balance-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <balance-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <balance-response>))
  "Converts a ROS message object to a list"
  (cl:list 'balance-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'balance)))
  'balance-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'balance)))
  'balance-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'balance)))
  "Returns string type for a service object of type '<balance>"
  "movement_utils/balance")