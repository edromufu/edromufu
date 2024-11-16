; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude rotate-request.msg.html

(cl:defclass <rotate-request> (roslisp-msg-protocol:ros-message)
  ((direction
    :reader direction
    :initarg :direction
    :type cl:fixnum
    :initform 0)
   (steps_number
    :reader steps_number
    :initarg :steps_number
    :type cl:fixnum
    :initform 0))
)

(cl:defclass rotate-request (<rotate-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <rotate-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'rotate-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<rotate-request> is deprecated: use movement_utils-srv:rotate-request instead.")))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <rotate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:direction-val is deprecated.  Use movement_utils-srv:direction instead.")
  (direction m))

(cl:ensure-generic-function 'steps_number-val :lambda-list '(m))
(cl:defmethod steps_number-val ((m <rotate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:steps_number-val is deprecated.  Use movement_utils-srv:steps_number instead.")
  (steps_number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <rotate-request>) ostream)
  "Serializes a message object of type '<rotate-request>"
  (cl:let* ((signed (cl:slot-value msg 'direction)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'steps_number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <rotate-request>) istream)
  "Deserializes a message object of type '<rotate-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'direction) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'steps_number) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<rotate-request>)))
  "Returns string type for a service object of type '<rotate-request>"
  "movement_utils/rotateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'rotate-request)))
  "Returns string type for a service object of type 'rotate-request"
  "movement_utils/rotateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<rotate-request>)))
  "Returns md5sum for a message object of type '<rotate-request>"
  "4589fa56bf3a1c197ab709f13c7adc75")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'rotate-request)))
  "Returns md5sum for a message object of type 'rotate-request"
  "4589fa56bf3a1c197ab709f13c7adc75")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<rotate-request>)))
  "Returns full string definition for message of type '<rotate-request>"
  (cl:format cl:nil "int8 direction~%int8 steps_number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'rotate-request)))
  "Returns full string definition for message of type 'rotate-request"
  (cl:format cl:nil "int8 direction~%int8 steps_number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <rotate-request>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <rotate-request>))
  "Converts a ROS message object to a list"
  (cl:list 'rotate-request
    (cl:cons ':direction (direction msg))
    (cl:cons ':steps_number (steps_number msg))
))
;//! \htmlinclude rotate-response.msg.html

(cl:defclass <rotate-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass rotate-response (<rotate-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <rotate-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'rotate-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<rotate-response> is deprecated: use movement_utils-srv:rotate-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <rotate-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <rotate-response>) ostream)
  "Serializes a message object of type '<rotate-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <rotate-response>) istream)
  "Deserializes a message object of type '<rotate-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<rotate-response>)))
  "Returns string type for a service object of type '<rotate-response>"
  "movement_utils/rotateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'rotate-response)))
  "Returns string type for a service object of type 'rotate-response"
  "movement_utils/rotateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<rotate-response>)))
  "Returns md5sum for a message object of type '<rotate-response>"
  "4589fa56bf3a1c197ab709f13c7adc75")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'rotate-response)))
  "Returns md5sum for a message object of type 'rotate-response"
  "4589fa56bf3a1c197ab709f13c7adc75")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<rotate-response>)))
  "Returns full string definition for message of type '<rotate-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'rotate-response)))
  "Returns full string definition for message of type 'rotate-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <rotate-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <rotate-response>))
  "Converts a ROS message object to a list"
  (cl:list 'rotate-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'rotate)))
  'rotate-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'rotate)))
  'rotate-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'rotate)))
  "Returns string type for a service object of type '<rotate>"
  "movement_utils/rotate")