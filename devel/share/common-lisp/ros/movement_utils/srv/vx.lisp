; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude vx-request.msg.html

(cl:defclass <vx-request> (roslisp-msg-protocol:ros-message)
  ((vx
    :reader vx
    :initarg :vx
    :type cl:float
    :initform 0.0)
   (distX
    :reader distX
    :initarg :distX
    :type cl:float
    :initform 0.0))
)

(cl:defclass vx-request (<vx-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vx-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vx-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<vx-request> is deprecated: use movement_utils-srv:vx-request instead.")))

(cl:ensure-generic-function 'vx-val :lambda-list '(m))
(cl:defmethod vx-val ((m <vx-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:vx-val is deprecated.  Use movement_utils-srv:vx instead.")
  (vx m))

(cl:ensure-generic-function 'distX-val :lambda-list '(m))
(cl:defmethod distX-val ((m <vx-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:distX-val is deprecated.  Use movement_utils-srv:distX instead.")
  (distX m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vx-request>) ostream)
  "Serializes a message object of type '<vx-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vx-request>) istream)
  "Deserializes a message object of type '<vx-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distX) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vx-request>)))
  "Returns string type for a service object of type '<vx-request>"
  "movement_utils/vxRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vx-request)))
  "Returns string type for a service object of type 'vx-request"
  "movement_utils/vxRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vx-request>)))
  "Returns md5sum for a message object of type '<vx-request>"
  "fc98f3eaa33f7560afd31582a184e752")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vx-request)))
  "Returns md5sum for a message object of type 'vx-request"
  "fc98f3eaa33f7560afd31582a184e752")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vx-request>)))
  "Returns full string definition for message of type '<vx-request>"
  (cl:format cl:nil "float32 vx~%float32 distX~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vx-request)))
  "Returns full string definition for message of type 'vx-request"
  (cl:format cl:nil "float32 vx~%float32 distX~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vx-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vx-request>))
  "Converts a ROS message object to a list"
  (cl:list 'vx-request
    (cl:cons ':vx (vx msg))
    (cl:cons ':distX (distX msg))
))
;//! \htmlinclude vx-response.msg.html

(cl:defclass <vx-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass vx-response (<vx-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vx-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vx-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<vx-response> is deprecated: use movement_utils-srv:vx-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <vx-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vx-response>) ostream)
  "Serializes a message object of type '<vx-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vx-response>) istream)
  "Deserializes a message object of type '<vx-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vx-response>)))
  "Returns string type for a service object of type '<vx-response>"
  "movement_utils/vxResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vx-response)))
  "Returns string type for a service object of type 'vx-response"
  "movement_utils/vxResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vx-response>)))
  "Returns md5sum for a message object of type '<vx-response>"
  "fc98f3eaa33f7560afd31582a184e752")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vx-response)))
  "Returns md5sum for a message object of type 'vx-response"
  "fc98f3eaa33f7560afd31582a184e752")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vx-response>)))
  "Returns full string definition for message of type '<vx-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vx-response)))
  "Returns full string definition for message of type 'vx-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vx-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vx-response>))
  "Converts a ROS message object to a list"
  (cl:list 'vx-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'vx)))
  'vx-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'vx)))
  'vx-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vx)))
  "Returns string type for a service object of type '<vx>"
  "movement_utils/vx")