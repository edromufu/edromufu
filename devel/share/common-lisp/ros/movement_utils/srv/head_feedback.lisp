; Auto-generated. Do not edit!


(cl:in-package movement_utils-srv)


;//! \htmlinclude head_feedback-request.msg.html

(cl:defclass <head_feedback-request> (roslisp-msg-protocol:ros-message)
  ((dont_use
    :reader dont_use
    :initarg :dont_use
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass head_feedback-request (<head_feedback-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <head_feedback-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'head_feedback-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<head_feedback-request> is deprecated: use movement_utils-srv:head_feedback-request instead.")))

(cl:ensure-generic-function 'dont_use-val :lambda-list '(m))
(cl:defmethod dont_use-val ((m <head_feedback-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:dont_use-val is deprecated.  Use movement_utils-srv:dont_use instead.")
  (dont_use m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <head_feedback-request>) ostream)
  "Serializes a message object of type '<head_feedback-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'dont_use) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <head_feedback-request>) istream)
  "Deserializes a message object of type '<head_feedback-request>"
    (cl:setf (cl:slot-value msg 'dont_use) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<head_feedback-request>)))
  "Returns string type for a service object of type '<head_feedback-request>"
  "movement_utils/head_feedbackRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'head_feedback-request)))
  "Returns string type for a service object of type 'head_feedback-request"
  "movement_utils/head_feedbackRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<head_feedback-request>)))
  "Returns md5sum for a message object of type '<head_feedback-request>"
  "a254b821d70340d5ccc8779b3f5e7d9c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'head_feedback-request)))
  "Returns md5sum for a message object of type 'head_feedback-request"
  "a254b821d70340d5ccc8779b3f5e7d9c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<head_feedback-request>)))
  "Returns full string definition for message of type '<head_feedback-request>"
  (cl:format cl:nil "bool dont_use~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'head_feedback-request)))
  "Returns full string definition for message of type 'head_feedback-request"
  (cl:format cl:nil "bool dont_use~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <head_feedback-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <head_feedback-request>))
  "Converts a ROS message object to a list"
  (cl:list 'head_feedback-request
    (cl:cons ':dont_use (dont_use msg))
))
;//! \htmlinclude head_feedback-response.msg.html

(cl:defclass <head_feedback-response> (roslisp-msg-protocol:ros-message)
  ((pos_vector
    :reader pos_vector
    :initarg :pos_vector
    :type (cl:vector cl:float)
   :initform (cl:make-array 2 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass head_feedback-response (<head_feedback-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <head_feedback-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'head_feedback-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_utils-srv:<head_feedback-response> is deprecated: use movement_utils-srv:head_feedback-response instead.")))

(cl:ensure-generic-function 'pos_vector-val :lambda-list '(m))
(cl:defmethod pos_vector-val ((m <head_feedback-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_utils-srv:pos_vector-val is deprecated.  Use movement_utils-srv:pos_vector instead.")
  (pos_vector m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <head_feedback-response>) ostream)
  "Serializes a message object of type '<head_feedback-response>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'pos_vector))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <head_feedback-response>) istream)
  "Deserializes a message object of type '<head_feedback-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<head_feedback-response>)))
  "Returns string type for a service object of type '<head_feedback-response>"
  "movement_utils/head_feedbackResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'head_feedback-response)))
  "Returns string type for a service object of type 'head_feedback-response"
  "movement_utils/head_feedbackResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<head_feedback-response>)))
  "Returns md5sum for a message object of type '<head_feedback-response>"
  "a254b821d70340d5ccc8779b3f5e7d9c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'head_feedback-response)))
  "Returns md5sum for a message object of type 'head_feedback-response"
  "a254b821d70340d5ccc8779b3f5e7d9c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<head_feedback-response>)))
  "Returns full string definition for message of type '<head_feedback-response>"
  (cl:format cl:nil "float32[2] pos_vector~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'head_feedback-response)))
  "Returns full string definition for message of type 'head_feedback-response"
  (cl:format cl:nil "float32[2] pos_vector~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <head_feedback-response>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'pos_vector) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <head_feedback-response>))
  "Converts a ROS message object to a list"
  (cl:list 'head_feedback-response
    (cl:cons ':pos_vector (pos_vector msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'head_feedback)))
  'head_feedback-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'head_feedback)))
  'head_feedback-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'head_feedback)))
  "Returns string type for a service object of type '<head_feedback>"
  "movement_utils/head_feedback")