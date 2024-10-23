; Auto-generated. Do not edit!


(cl:in-package movement_msgs-msg)


;//! \htmlinclude WalkingPositionsMsg.msg.html

(cl:defclass <WalkingPositionsMsg> (roslisp-msg-protocol:ros-message)
  ((positions
    :reader positions
    :initarg :positions
    :type (cl:vector cl:float)
   :initform (cl:make-array 12 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass WalkingPositionsMsg (<WalkingPositionsMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WalkingPositionsMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WalkingPositionsMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement_msgs-msg:<WalkingPositionsMsg> is deprecated: use movement_msgs-msg:WalkingPositionsMsg instead.")))

(cl:ensure-generic-function 'positions-val :lambda-list '(m))
(cl:defmethod positions-val ((m <WalkingPositionsMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement_msgs-msg:positions-val is deprecated.  Use movement_msgs-msg:positions instead.")
  (positions m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WalkingPositionsMsg>) ostream)
  "Serializes a message object of type '<WalkingPositionsMsg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'positions))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WalkingPositionsMsg>) istream)
  "Deserializes a message object of type '<WalkingPositionsMsg>"
  (cl:setf (cl:slot-value msg 'positions) (cl:make-array 12))
  (cl:let ((vals (cl:slot-value msg 'positions)))
    (cl:dotimes (i 12)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WalkingPositionsMsg>)))
  "Returns string type for a message object of type '<WalkingPositionsMsg>"
  "movement_msgs/WalkingPositionsMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WalkingPositionsMsg)))
  "Returns string type for a message object of type 'WalkingPositionsMsg"
  "movement_msgs/WalkingPositionsMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WalkingPositionsMsg>)))
  "Returns md5sum for a message object of type '<WalkingPositionsMsg>"
  "432ba4694a7ccfad78b66057edbee5ed")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WalkingPositionsMsg)))
  "Returns md5sum for a message object of type 'WalkingPositionsMsg"
  "432ba4694a7ccfad78b66057edbee5ed")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WalkingPositionsMsg>)))
  "Returns full string definition for message of type '<WalkingPositionsMsg>"
  (cl:format cl:nil "float64[12] positions~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WalkingPositionsMsg)))
  "Returns full string definition for message of type 'WalkingPositionsMsg"
  (cl:format cl:nil "float64[12] positions~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WalkingPositionsMsg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'positions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WalkingPositionsMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'WalkingPositionsMsg
    (cl:cons ':positions (positions msg))
))
