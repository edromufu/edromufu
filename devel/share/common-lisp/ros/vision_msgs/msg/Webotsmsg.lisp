; Auto-generated. Do not edit!


(cl:in-package vision_msgs-msg)


;//! \htmlinclude Webotsmsg.msg.html

(cl:defclass <Webotsmsg> (roslisp-msg-protocol:ros-message)
  ((searching
    :reader searching
    :initarg :searching
    :type cl:boolean
    :initform cl:nil)
   (fps
    :reader fps
    :initarg :fps
    :type cl:fixnum
    :initform 0)
   (ball
    :reader ball
    :initarg :ball
    :type vision_msgs-msg:Ball
    :initform (cl:make-instance 'vision_msgs-msg:Ball))
   (leftgoalpost
    :reader leftgoalpost
    :initarg :leftgoalpost
    :type vision_msgs-msg:Leftgoalpost
    :initform (cl:make-instance 'vision_msgs-msg:Leftgoalpost))
   (rightgoalpost
    :reader rightgoalpost
    :initarg :rightgoalpost
    :type vision_msgs-msg:Rightgoalpost
    :initform (cl:make-instance 'vision_msgs-msg:Rightgoalpost)))
)

(cl:defclass Webotsmsg (<Webotsmsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Webotsmsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Webotsmsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision_msgs-msg:<Webotsmsg> is deprecated: use vision_msgs-msg:Webotsmsg instead.")))

(cl:ensure-generic-function 'searching-val :lambda-list '(m))
(cl:defmethod searching-val ((m <Webotsmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:searching-val is deprecated.  Use vision_msgs-msg:searching instead.")
  (searching m))

(cl:ensure-generic-function 'fps-val :lambda-list '(m))
(cl:defmethod fps-val ((m <Webotsmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:fps-val is deprecated.  Use vision_msgs-msg:fps instead.")
  (fps m))

(cl:ensure-generic-function 'ball-val :lambda-list '(m))
(cl:defmethod ball-val ((m <Webotsmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:ball-val is deprecated.  Use vision_msgs-msg:ball instead.")
  (ball m))

(cl:ensure-generic-function 'leftgoalpost-val :lambda-list '(m))
(cl:defmethod leftgoalpost-val ((m <Webotsmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:leftgoalpost-val is deprecated.  Use vision_msgs-msg:leftgoalpost instead.")
  (leftgoalpost m))

(cl:ensure-generic-function 'rightgoalpost-val :lambda-list '(m))
(cl:defmethod rightgoalpost-val ((m <Webotsmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:rightgoalpost-val is deprecated.  Use vision_msgs-msg:rightgoalpost instead.")
  (rightgoalpost m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Webotsmsg>) ostream)
  "Serializes a message object of type '<Webotsmsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'searching) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'fps)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ball) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'leftgoalpost) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'rightgoalpost) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Webotsmsg>) istream)
  "Deserializes a message object of type '<Webotsmsg>"
    (cl:setf (cl:slot-value msg 'searching) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'fps)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ball) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'leftgoalpost) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'rightgoalpost) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Webotsmsg>)))
  "Returns string type for a message object of type '<Webotsmsg>"
  "vision_msgs/Webotsmsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Webotsmsg)))
  "Returns string type for a message object of type 'Webotsmsg"
  "vision_msgs/Webotsmsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Webotsmsg>)))
  "Returns md5sum for a message object of type '<Webotsmsg>"
  "2b9c0baf80135ab319a9a2d5f79a6c9a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Webotsmsg)))
  "Returns md5sum for a message object of type 'Webotsmsg"
  "2b9c0baf80135ab319a9a2d5f79a6c9a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Webotsmsg>)))
  "Returns full string definition for message of type '<Webotsmsg>"
  (cl:format cl:nil "bool searching~%uint8 fps~%vision_msgs/Ball ball~%vision_msgs/Leftgoalpost leftgoalpost~%vision_msgs/Rightgoalpost rightgoalpost~%================================================================================~%MSG: vision_msgs/Ball~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%================================================================================~%MSG: vision_msgs/Leftgoalpost~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%~%================================================================================~%MSG: vision_msgs/Rightgoalpost~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Webotsmsg)))
  "Returns full string definition for message of type 'Webotsmsg"
  (cl:format cl:nil "bool searching~%uint8 fps~%vision_msgs/Ball ball~%vision_msgs/Leftgoalpost leftgoalpost~%vision_msgs/Rightgoalpost rightgoalpost~%================================================================================~%MSG: vision_msgs/Ball~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%================================================================================~%MSG: vision_msgs/Leftgoalpost~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%~%================================================================================~%MSG: vision_msgs/Rightgoalpost~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Webotsmsg>))
  (cl:+ 0
     1
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ball))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'leftgoalpost))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'rightgoalpost))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Webotsmsg>))
  "Converts a ROS message object to a list"
  (cl:list 'Webotsmsg
    (cl:cons ':searching (searching msg))
    (cl:cons ':fps (fps msg))
    (cl:cons ':ball (ball msg))
    (cl:cons ':leftgoalpost (leftgoalpost msg))
    (cl:cons ':rightgoalpost (rightgoalpost msg))
))
