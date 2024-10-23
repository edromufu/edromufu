; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude walk_forward-request.msg.html

(cl:defclass <walk_forward-request> (roslisp-msg-protocol:ros-message)
  ((support_foot
    :reader support_foot
    :initarg :support_foot
    :type cl:fixnum
    :initform 0)
   (steps_number
    :reader steps_number
    :initarg :steps_number
    :type cl:fixnum
    :initform 0))
)

(cl:defclass walk_forward-request (<walk_forward-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <walk_forward-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'walk_forward-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<walk_forward-request> is deprecated: use movement_utils-srv:walk_forward-request instead.")))

(cl:ensure-generic-function 'support_foot-val :lambda-list '(m))
(cl:defmethod support_foot-val ((m <walk_forward-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:support_foot-val is deprecated.  Use movement_utils-srv:support_foot instead.")
  (support_foot m))

(cl:ensure-generic-function 'steps_number-val :lambda-list '(m))
(cl:defmethod steps_number-val ((m <walk_forward-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:steps_number-val is deprecated.  Use movement_utils-srv:steps_number instead.")
  (steps_number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <walk_forward-request>) ostream)
  "Serializes a message object of type '<walk_forward-request>"
  (cl:let* ((signed (cl:slot-value msg 'support_foot)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'steps_number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <walk_forward-request>) istream)
  "Deserializes a message object of type '<walk_forward-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'support_foot) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'steps_number) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<walk_forward-request>)))
  "Returns string type for a service object of type '<walk_forward-request>"
  "movement_utils/walk_forwardRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'walk_forward-request)))
  "Returns string type for a service object of type 'walk_forward-request"
  "movement_utils/walk_forwardRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<walk_forward-request>)))
  "Returns md5sum for a message object of type '<walk_forward-request>"
  "4e96d691545ef71c6c6ffe49fb624ea4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'walk_forward-request)))
  "Returns md5sum for a message object of type 'walk_forward-request"
  "4e96d691545ef71c6c6ffe49fb624ea4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<walk_forward-request>)))
  "Returns full string definition for message of type '<walk_forward-request>"
  (cl:format cl:nil "int8 support_foot~%int8 steps_number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'walk_forward-request)))
  "Returns full string definition for message of type 'walk_forward-request"
  (cl:format cl:nil "int8 support_foot~%int8 steps_number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <walk_forward-request>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <walk_forward-request>))
  "Converts a ROS message object to a list"
  (cl:list 'walk_forward-request
    (cl:cons ':support_foot (support_foot msg))
    (cl:cons ':steps_number (steps_number msg))
))
;//! \htmlinclude walk_forward-response.msg.html

(cl:defclass <walk_forward-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass walk_forward-response (<walk_forward-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <walk_forward-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'walk_forward-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<walk_forward-response> is deprecated: use movement_utils-srv:walk_forward-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <walk_forward-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <walk_forward-response>) ostream)
  "Serializes a message object of type '<walk_forward-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <walk_forward-response>) istream)
  "Deserializes a message object of type '<walk_forward-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<walk_forward-response>)))
  "Returns string type for a service object of type '<walk_forward-response>"
  "movement_utils/walk_forwardResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'walk_forward-response)))
  "Returns string type for a service object of type 'walk_forward-response"
  "movement_utils/walk_forwardResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<walk_forward-response>)))
  "Returns md5sum for a message object of type '<walk_forward-response>"
  "4e96d691545ef71c6c6ffe49fb624ea4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'walk_forward-response)))
  "Returns md5sum for a message object of type 'walk_forward-response"
  "4e96d691545ef71c6c6ffe49fb624ea4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<walk_forward-response>)))
  "Returns full string definition for message of type '<walk_forward-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'walk_forward-response)))
  "Returns full string definition for message of type 'walk_forward-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <walk_forward-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <walk_forward-response>))
  "Converts a ROS message object to a list"
  (cl:list 'walk_forward-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'walk_forward)))
  'walk_forward-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'walk_forward)))
  'walk_forward-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'walk_forward)))
  "Returns string type for a service object of type '<walk_forward>"
  "movement_utils/walk_forward")