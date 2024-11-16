; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude enable_torque-request.msg.html

(cl:defclass <enable_torque-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:boolean
    :initform cl:nil)
   (motor_ids
    :reader motor_ids
    :initarg :motor_ids
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass enable_torque-request (<enable_torque-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <enable_torque-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'enable_torque-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<enable_torque-request> is deprecated: use movement_utils-srv:enable_torque-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <enable_torque-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:data-val is deprecated.  Use movement_utils-srv:data instead.")
  (data m))

(cl:ensure-generic-function 'motor_ids-val :lambda-list '(m))
(cl:defmethod motor_ids-val ((m <enable_torque-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:motor_ids-val is deprecated.  Use movement_utils-srv:motor_ids instead.")
  (motor_ids m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <enable_torque-request>) ostream)
  "Serializes a message object of type '<enable_torque-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'data) 1 0)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'motor_ids))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'motor_ids))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <enable_torque-request>) istream)
  "Deserializes a message object of type '<enable_torque-request>"
    (cl:setf (cl:slot-value msg 'data) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'motor_ids) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'motor_ids)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<enable_torque-request>)))
  "Returns string type for a service object of type '<enable_torque-request>"
  "movement_utils/enable_torqueRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enable_torque-request)))
  "Returns string type for a service object of type 'enable_torque-request"
  "movement_utils/enable_torqueRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<enable_torque-request>)))
  "Returns md5sum for a message object of type '<enable_torque-request>"
  "56c16441f9caa9412e348ec2e61432df")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'enable_torque-request)))
  "Returns md5sum for a message object of type 'enable_torque-request"
  "56c16441f9caa9412e348ec2e61432df")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<enable_torque-request>)))
  "Returns full string definition for message of type '<enable_torque-request>"
  (cl:format cl:nil "bool data~%int8[] motor_ids~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'enable_torque-request)))
  "Returns full string definition for message of type 'enable_torque-request"
  (cl:format cl:nil "bool data~%int8[] motor_ids~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <enable_torque-request>))
  (cl:+ 0
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'motor_ids) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <enable_torque-request>))
  "Converts a ROS message object to a list"
  (cl:list 'enable_torque-request
    (cl:cons ':data (data msg))
    (cl:cons ':motor_ids (motor_ids msg))
))
;//! \htmlinclude enable_torque-response.msg.html

(cl:defclass <enable_torque-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass enable_torque-response (<enable_torque-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <enable_torque-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'enable_torque-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<enable_torque-response> is deprecated: use movement_utils-srv:enable_torque-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <enable_torque-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:success-val is deprecated.  Use movement_utils-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <enable_torque-response>) ostream)
  "Serializes a message object of type '<enable_torque-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <enable_torque-response>) istream)
  "Deserializes a message object of type '<enable_torque-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<enable_torque-response>)))
  "Returns string type for a service object of type '<enable_torque-response>"
  "movement_utils/enable_torqueResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enable_torque-response)))
  "Returns string type for a service object of type 'enable_torque-response"
  "movement_utils/enable_torqueResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<enable_torque-response>)))
  "Returns md5sum for a message object of type '<enable_torque-response>"
  "56c16441f9caa9412e348ec2e61432df")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'enable_torque-response)))
  "Returns md5sum for a message object of type 'enable_torque-response"
  "56c16441f9caa9412e348ec2e61432df")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<enable_torque-response>)))
  "Returns full string definition for message of type '<enable_torque-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'enable_torque-response)))
  "Returns full string definition for message of type 'enable_torque-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <enable_torque-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <enable_torque-response>))
  "Converts a ROS message object to a list"
  (cl:list 'enable_torque-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'enable_torque)))
  'enable_torque-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'enable_torque)))
  'enable_torque-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enable_torque)))
  "Returns string type for a service object of type '<enable_torque>"
  "movement_utils/enable_torque")