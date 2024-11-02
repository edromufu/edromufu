;; Auto-generated. Do not edit!


(when (boundp 'vision_msgs::Objects)
  (if (not (find-package "VISION_MSGS"))
    (make-package "VISION_MSGS"))
  (shadow 'Objects (find-package "VISION_MSGS")))
(unless (find-package "VISION_MSGS::OBJECTS")
  (make-package "VISION_MSGS::OBJECTS"))

(in-package "ROS")
;;//! \htmlinclude Objects.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass vision_msgs::Objects
  :super ros::object
  :slots (_ball _goal _robots _image ))

(defmethod vision_msgs::Objects
  (:init
   (&key
    ((:ball __ball) (instance vision_msgs::Ball :init))
    ((:goal __goal) (instance vision_msgs::Goal :init))
    ((:robots __robots) ())
    ((:image __image) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _ball __ball)
   (setq _goal __goal)
   (setq _robots __robots)
   (setq _image __image)
   self)
  (:ball
   (&rest __ball)
   (if (keywordp (car __ball))
       (send* _ball __ball)
     (progn
       (if __ball (setq _ball (car __ball)))
       _ball)))
  (:goal
   (&rest __goal)
   (if (keywordp (car __goal))
       (send* _goal __goal)
     (progn
       (if __goal (setq _goal (car __goal)))
       _goal)))
  (:robots
   (&rest __robots)
   (if (keywordp (car __robots))
       (send* _robots __robots)
     (progn
       (if __robots (setq _robots (car __robots)))
       _robots)))
  (:image
   (&rest __image)
   (if (keywordp (car __image))
       (send* _image __image)
     (progn
       (if __image (setq _image (car __image)))
       _image)))
  (:serialization-length
   ()
   (+
    ;; vision_msgs/Ball _ball
    (send _ball :serialization-length)
    ;; vision_msgs/Goal _goal
    (send _goal :serialization-length)
    ;; vision_msgs/Robot[] _robots
    (apply #'+ (send-all _robots :serialization-length)) 4
    ;; sensor_msgs/Image _image
    (send _image :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; vision_msgs/Ball _ball
       (send _ball :serialize s)
     ;; vision_msgs/Goal _goal
       (send _goal :serialize s)
     ;; vision_msgs/Robot[] _robots
     (write-long (length _robots) s)
     (dolist (elem _robots)
       (send elem :serialize s)
       )
     ;; sensor_msgs/Image _image
       (send _image :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; vision_msgs/Ball _ball
     (send _ball :deserialize buf ptr-) (incf ptr- (send _ball :serialization-length))
   ;; vision_msgs/Goal _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;; vision_msgs/Robot[] _robots
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _robots (let (r) (dotimes (i n) (push (instance vision_msgs::Robot :init) r)) r))
     (dolist (elem- _robots)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; sensor_msgs/Image _image
     (send _image :deserialize buf ptr-) (incf ptr- (send _image :serialization-length))
   ;;
   self)
  )

(setf (get vision_msgs::Objects :md5sum-) "19f71dba810720091bb37489652c025c")
(setf (get vision_msgs::Objects :datatype-) "vision_msgs/Objects")
(setf (get vision_msgs::Objects :definition-)
      "vision_msgs/Ball ball
vision_msgs/Goal goal
vision_msgs/Robot[] robots
sensor_msgs/Image image
================================================================================
MSG: vision_msgs/Ball
bool found
int32 x
int32 y
int32 roi_width
int32 roi_height
================================================================================
MSG: vision_msgs/Goal
bool found
int32 x
int32 y
================================================================================
MSG: vision_msgs/Robot
int32 x
int32 y
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :vision_msgs/Objects "19f71dba810720091bb37489652c025c")


