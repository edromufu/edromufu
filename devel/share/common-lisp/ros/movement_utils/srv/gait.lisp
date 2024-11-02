; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude gait-request.msg.html

(cl:defclass <gait-request> (roslisp-msg-protocol:ros-message)
  ((steps_number
    :reader steps_number
    :initarg :steps_number
    :type cl:fixnum
    :initform 0)
   (step_height
    :reader step_height
    :initarg :step_height
    :type cl:float
    :initform 0.0))
)

(cl:defclass gait-request (<gait-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gait-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gait-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<gait-request> is deprecated: use movement_utils-srv:gait-request instead.")))

(cl:ensure-generic-function 'steps_number-val :lambda-list '(m))
(cl:defmethod steps_number-val ((m <gait-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:steps_number-val is deprecated.  Use movement_utils-srv:steps_number instead.")
  (steps_number m))

(cl:ensure-generic-function 'step_height-val :lambda-list '(m))
(cl:defmethod step_height-val ((m <gait-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:step_height-val is deprecated.  Use movement_utils-srv:step_height instead.")
  (step_height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gait-request>) ostream)
  "Serializes a message object of type '<gait-request>"
  (cl:let* ((signed (cl:slot-value msg 'steps_number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'step_height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gait-request>) istream)
  "Deserializes a message object of type '<gait-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'steps_number) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'step_height) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gait-request>)))
  "Returns string type for a service object of type '<gait-request>"
  "movement_utils/gaitRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gait-request)))
  "Returns string type for a service object of type 'gait-request"
  "movement_utils/gaitRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gait-request>)))
  "Returns md5sum for a message object of type '<gait-request>"
  "372f208eec6910dde42b51ee38202481")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gait-request)))
  "Returns md5sum for a message object of type 'gait-request"
  "372f208eec6910dde42b51ee38202481")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gait-request>)))
  "Returns full string definition for message of type '<gait-request>"
  (cl:format cl:nil "int8 steps_number~%float32 step_height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gait-request)))
  "Returns full string definition for message of type 'gait-request"
  (cl:format cl:nil "int8 steps_number~%float32 step_height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gait-request>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gait-request>))
  "Converts a ROS message object to a list"
  (cl:list 'gait-request
    (cl:cons ':steps_number (steps_number msg))
    (cl:cons ':step_height (step_height msg))
))
;//! \htmlinclude gait-response.msg.html

(cl:defclass <gait-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass gait-response (<gait-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gait-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gait-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<gait-response> is deprecated: use movement_utils-srv:gait-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <gait-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gait-response>) ostream)
  "Serializes a message object of type '<gait-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gait-response>) istream)
  "Deserializes a message object of type '<gait-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gait-response>)))
  "Returns string type for a service object of type '<gait-response>"
  "movement_utils/gaitResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gait-response)))
  "Returns string type for a service object of type 'gait-response"
  "movement_utils/gaitResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gait-response>)))
  "Returns md5sum for a message object of type '<gait-response>"
  "372f208eec6910dde42b51ee38202481")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gait-response)))
  "Returns md5sum for a message object of type 'gait-response"
  "372f208eec6910dde42b51ee38202481")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gait-response>)))
  "Returns full string definition for message of type '<gait-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gait-response)))
  "Returns full string definition for message of type 'gait-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gait-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gait-response>))
  "Converts a ROS message object to a list"
  (cl:list 'gait-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'gait)))
  'gait-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'gait)))
  'gait-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gait)))
  "Returns string type for a service object of type '<gait>"
  "movement_utils/gait")