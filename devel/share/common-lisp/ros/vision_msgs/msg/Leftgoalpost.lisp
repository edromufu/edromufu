; Auto-generated. Do not edit!


(cl:in-package vision_msgs-msg)


;//! \htmlinclude Leftgoalpost.msg.html

(cl:defclass <Leftgoalpost> (roslisp-msg-protocol:ros-message)
  ((found
    :reader found
    :initarg :found
    :type cl:boolean
    :initform cl:nil)
   (x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (roi_width
    :reader roi_width
    :initarg :roi_width
    :type cl:integer
    :initform 0)
   (roi_height
    :reader roi_height
    :initarg :roi_height
    :type cl:integer
    :initform 0))
)

(cl:defclass Leftgoalpost (<Leftgoalpost>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Leftgoalpost>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Leftgoalpost)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision_msgs-msg:<Leftgoalpost> is deprecated: use vision_msgs-msg:Leftgoalpost instead.")))

(cl:ensure-generic-function 'found-val :lambda-list '(m))
(cl:defmethod found-val ((m <Leftgoalpost>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:found-val is deprecated.  Use vision_msgs-msg:found instead.")
  (found m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Leftgoalpost>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:x-val is deprecated.  Use vision_msgs-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Leftgoalpost>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:y-val is deprecated.  Use vision_msgs-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'roi_width-val :lambda-list '(m))
(cl:defmethod roi_width-val ((m <Leftgoalpost>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:roi_width-val is deprecated.  Use vision_msgs-msg:roi_width instead.")
  (roi_width m))

(cl:ensure-generic-function 'roi_height-val :lambda-list '(m))
(cl:defmethod roi_height-val ((m <Leftgoalpost>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:roi_height-val is deprecated.  Use vision_msgs-msg:roi_height instead.")
  (roi_height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Leftgoalpost>) ostream)
  "Serializes a message object of type '<Leftgoalpost>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'found) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'roi_width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'roi_height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Leftgoalpost>) istream)
  "Deserializes a message object of type '<Leftgoalpost>"
    (cl:setf (cl:slot-value msg 'found) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'roi_width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'roi_height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Leftgoalpost>)))
  "Returns string type for a message object of type '<Leftgoalpost>"
  "vision_msgs/Leftgoalpost")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Leftgoalpost)))
  "Returns string type for a message object of type 'Leftgoalpost"
  "vision_msgs/Leftgoalpost")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Leftgoalpost>)))
  "Returns md5sum for a message object of type '<Leftgoalpost>"
  "593e6a8c66231b4fe6d1d33cf452902c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Leftgoalpost)))
  "Returns md5sum for a message object of type 'Leftgoalpost"
  "593e6a8c66231b4fe6d1d33cf452902c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Leftgoalpost>)))
  "Returns full string definition for message of type '<Leftgoalpost>"
  (cl:format cl:nil "bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Leftgoalpost)))
  "Returns full string definition for message of type 'Leftgoalpost"
  (cl:format cl:nil "bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Leftgoalpost>))
  (cl:+ 0
     1
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Leftgoalpost>))
  "Converts a ROS message object to a list"
  (cl:list 'Leftgoalpost
    (cl:cons ':found (found msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':roi_width (roi_width msg))
    (cl:cons ':roi_height (roi_height msg))
))
