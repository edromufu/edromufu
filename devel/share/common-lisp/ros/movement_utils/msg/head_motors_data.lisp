; Auto-generated. Do not edit!


(cl:in-package movement_utils-msg)


;//! \htmlinclude head_motors_data.msg.html

(cl:defclass <head_motors_data> (roslisp-msg-protocol:ros-message)
  ((pos_vector
    :reader pos_vector
    :initarg :pos_vector
    :type (cl:vector cl:float)
   :initform (cl:make-array 2 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass head_motors_data (<head_motors_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <head_motors_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'head_motors_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-msg:<head_motors_data> is deprecated: use movement_utils-msg:head_motors_data instead.")))

(cl:ensure-generic-function 'pos_vector-val :lambda-list '(m))
(cl:defmethod pos_vector-val ((m <head_motors_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-msg:pos_vector-val is deprecated.  Use movement_utils-msg:pos_vector instead.")
  (pos_vector m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <head_motors_data>) ostream)
  "Serializes a message object of type '<head_motors_data>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'pos_vector))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <head_motors_data>) istream)
  "Deserializes a message object of type '<head_motors_data>"
  (cl:setf (cl:slot-value msg 'pos_vector) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'pos_vector)))
    (cl:dotimes (i 2)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<head_motors_data>)))
  "Returns string type for a message object of type '<head_motors_data>"
  "movement_utils/head_motors_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'head_motors_data)))
  "Returns string type for a message object of type 'head_motors_data"
  "movement_utils/head_motors_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<head_motors_data>)))
  "Returns md5sum for a message object of type '<head_motors_data>"
  "019f44c03fbd0840875f997c96bee773")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'head_motors_data)))
  "Returns md5sum for a message object of type 'head_motors_data"
  "019f44c03fbd0840875f997c96bee773")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<head_motors_data>)))
  "Returns full string definition for message of type '<head_motors_data>"
  (cl:format cl:nil "float32[2] pos_vector~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'head_motors_data)))
  "Returns full string definition for message of type 'head_motors_data"
  (cl:format cl:nil "float32[2] pos_vector~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <head_motors_data>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'pos_vector) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <head_motors_data>))
  "Converts a ROS message object to a list"
  (cl:list 'head_motors_data
    (cl:cons ':pos_vector (pos_vector msg))
))
