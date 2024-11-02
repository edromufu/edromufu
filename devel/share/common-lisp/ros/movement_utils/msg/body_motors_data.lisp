; Auto-generated. Do not edit!


(cl:in-package movement_utils-msg)


;//! \htmlinclude body_motors_data.msg.html

(cl:defclass <body_motors_data> (roslisp-msg-protocol:ros-message)
  ((pos_vector
    :reader pos_vector
    :initarg :pos_vector
    :type (cl:vector cl:float)
   :initform (cl:make-array 18 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass body_motors_data (<body_motors_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <body_motors_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'body_motors_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-msg:<body_motors_data> is deprecated: use movement_utils-msg:body_motors_data instead.")))

(cl:ensure-generic-function 'pos_vector-val :lambda-list '(m))
(cl:defmethod pos_vector-val ((m <body_motors_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-msg:pos_vector-val is deprecated.  Use movement_utils-msg:pos_vector instead.")
  (pos_vector m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <body_motors_data>) ostream)
  "Serializes a message object of type '<body_motors_data>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'pos_vector))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <body_motors_data>) istream)
  "Deserializes a message object of type '<body_motors_data>"
  (cl:setf (cl:slot-value msg 'pos_vector) (cl:make-array 18))
  (cl:let ((vals (cl:slot-value msg 'pos_vector)))
    (cl:dotimes (i 18)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<body_motors_data>)))
  "Returns string type for a message object of type '<body_motors_data>"
  "movement_utils/body_motors_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'body_motors_data)))
  "Returns string type for a message object of type 'body_motors_data"
  "movement_utils/body_motors_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<body_motors_data>)))
  "Returns md5sum for a message object of type '<body_motors_data>"
  "18af1fa9d2e7d06f4ff52d42169a41bd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'body_motors_data)))
  "Returns md5sum for a message object of type 'body_motors_data"
  "18af1fa9d2e7d06f4ff52d42169a41bd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<body_motors_data>)))
  "Returns full string definition for message of type '<body_motors_data>"
  (cl:format cl:nil "float32[18] pos_vector~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'body_motors_data)))
  "Returns full string definition for message of type 'body_motors_data"
  (cl:format cl:nil "float32[18] pos_vector~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <body_motors_data>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'pos_vector) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <body_motors_data>))
  "Converts a ROS message object to a list"
  (cl:list 'body_motors_data
    (cl:cons ':pos_vector (pos_vector msg))
))
