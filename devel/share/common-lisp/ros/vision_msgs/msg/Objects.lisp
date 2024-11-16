; Auto-generated. Do not edit!


(cl:in-package vision_msgs-msg)


;//! \htmlinclude Objects.msg.html

(cl:defclass <Objects> (roslisp-msg-protocol:ros-message)
  ((ball
    :reader ball
    :initarg :ball
    :type vision_msgs-msg:Ball
    :initform (cl:make-instance 'vision_msgs-msg:Ball))
   (goal
    :reader goal
    :initarg :goal
    :type vision_msgs-msg:Goal
    :initform (cl:make-instance 'vision_msgs-msg:Goal))
   (robots
    :reader robots
    :initarg :robots
    :type (cl:vector vision_msgs-msg:Robot)
   :initform (cl:make-array 0 :element-type 'vision_msgs-msg:Robot :initial-element (cl:make-instance 'vision_msgs-msg:Robot)))
   (image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass Objects (<Objects>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Objects>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Objects)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision_msgs-msg:<Objects> is deprecated: use vision_msgs-msg:Objects instead.")))

(cl:ensure-generic-function 'ball-val :lambda-list '(m))
(cl:defmethod ball-val ((m <Objects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:ball-val is deprecated.  Use vision_msgs-msg:ball instead.")
  (ball m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <Objects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:goal-val is deprecated.  Use vision_msgs-msg:goal instead.")
  (goal m))

(cl:ensure-generic-function 'robots-val :lambda-list '(m))
(cl:defmethod robots-val ((m <Objects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:robots-val is deprecated.  Use vision_msgs-msg:robots instead.")
  (robots m))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <Objects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_msgs-msg:image-val is deprecated.  Use vision_msgs-msg:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Objects>) ostream)
  "Serializes a message object of type '<Objects>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ball) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'robots))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'robots))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Objects>) istream)
  "Deserializes a message object of type '<Objects>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ball) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'robots) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'robots)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'vision_msgs-msg:Robot))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Objects>)))
  "Returns string type for a message object of type '<Objects>"
  "vision_msgs/Objects")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Objects)))
  "Returns string type for a message object of type 'Objects"
  "vision_msgs/Objects")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Objects>)))
  "Returns md5sum for a message object of type '<Objects>"
  "19f71dba810720091bb37489652c025c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Objects)))
  "Returns md5sum for a message object of type 'Objects"
  "19f71dba810720091bb37489652c025c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Objects>)))
  "Returns full string definition for message of type '<Objects>"
  (cl:format cl:nil "vision_msgs/Ball ball~%vision_msgs/Goal goal~%vision_msgs/Robot[] robots~%sensor_msgs/Image image~%================================================================================~%MSG: vision_msgs/Ball~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%================================================================================~%MSG: vision_msgs/Goal~%bool found~%int32 x~%int32 y~%================================================================================~%MSG: vision_msgs/Robot~%int32 x~%int32 y~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Objects)))
  "Returns full string definition for message of type 'Objects"
  (cl:format cl:nil "vision_msgs/Ball ball~%vision_msgs/Goal goal~%vision_msgs/Robot[] robots~%sensor_msgs/Image image~%================================================================================~%MSG: vision_msgs/Ball~%bool found~%int32 x~%int32 y~%int32 roi_width~%int32 roi_height~%================================================================================~%MSG: vision_msgs/Goal~%bool found~%int32 x~%int32 y~%================================================================================~%MSG: vision_msgs/Robot~%int32 x~%int32 y~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Objects>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ball))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'robots) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Objects>))
  "Converts a ROS message object to a list"
  (cl:list 'Objects
    (cl:cons ':ball (ball msg))
    (cl:cons ':goal (goal msg))
    (cl:cons ':robots (robots msg))
    (cl:cons ':image (image msg))
))
