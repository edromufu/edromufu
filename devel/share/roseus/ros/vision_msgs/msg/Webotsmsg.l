;; Auto-generated. Do not edit!


(when (boundp 'vision_msgs::Webotsmsg)
  (if (not (find-package "VISION_MSGS"))
    (make-package "VISION_MSGS"))
  (shadow 'Webotsmsg (find-package "VISION_MSGS")))
(unless (find-package "VISION_MSGS::WEBOTSMSG")
  (make-package "VISION_MSGS::WEBOTSMSG"))

(in-package "ROS")
;;//! \htmlinclude Webotsmsg.msg.html


(defclass vision_msgs::Webotsmsg
  :super ros::object
  :slots (_searching _fps _ball _leftgoalpost _rightgoalpost ))

(defmethod vision_msgs::Webotsmsg
  (:init
   (&key
    ((:searching __searching) nil)
    ((:fps __fps) 0)
    ((:ball __ball) (instance vision_msgs::Ball :init))
    ((:leftgoalpost __leftgoalpost) (instance vision_msgs::Leftgoalpost :init))
    ((:rightgoalpost __rightgoalpost) (instance vision_msgs::Rightgoalpost :init))
    )
   (send-super :init)
   (setq _searching __searching)
   (setq _fps (round __fps))
   (setq _ball __ball)
   (setq _leftgoalpost __leftgoalpost)
   (setq _rightgoalpost __rightgoalpost)
   self)
  (:searching
   (&optional (__searching :null))
   (if (not (eq __searching :null)) (setq _searching __searching)) _searching)
  (:fps
   (&optional __fps)
   (if __fps (setq _fps __fps)) _fps)
  (:ball
   (&rest __ball)
   (if (keywordp (car __ball))
       (send* _ball __ball)
     (progn
       (if __ball (setq _ball (car __ball)))
       _ball)))
  (:leftgoalpost
   (&rest __leftgoalpost)
   (if (keywordp (car __leftgoalpost))
       (send* _leftgoalpost __leftgoalpost)
     (progn
       (if __leftgoalpost (setq _leftgoalpost (car __leftgoalpost)))
       _leftgoalpost)))
  (:rightgoalpost
   (&rest __rightgoalpost)
   (if (keywordp (car __rightgoalpost))
       (send* _rightgoalpost __rightgoalpost)
     (progn
       (if __rightgoalpost (setq _rightgoalpost (car __rightgoalpost)))
       _rightgoalpost)))
  (:serialization-length
   ()
   (+
    ;; bool _searching
    1
    ;; uint8 _fps
    1
    ;; vision_msgs/Ball _ball
    (send _ball :serialization-length)
    ;; vision_msgs/Leftgoalpost _leftgoalpost
    (send _leftgoalpost :serialization-length)
    ;; vision_msgs/Rightgoalpost _rightgoalpost
    (send _rightgoalpost :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _searching
       (if _searching (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _fps
       (write-byte _fps s)
     ;; vision_msgs/Ball _ball
       (send _ball :serialize s)
     ;; vision_msgs/Leftgoalpost _leftgoalpost
       (send _leftgoalpost :serialize s)
     ;; vision_msgs/Rightgoalpost _rightgoalpost
       (send _rightgoalpost :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _searching
     (setq _searching (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _fps
     (setq _fps (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; vision_msgs/Ball _ball
     (send _ball :deserialize buf ptr-) (incf ptr- (send _ball :serialization-length))
   ;; vision_msgs/Leftgoalpost _leftgoalpost
     (send _leftgoalpost :deserialize buf ptr-) (incf ptr- (send _leftgoalpost :serialization-length))
   ;; vision_msgs/Rightgoalpost _rightgoalpost
     (send _rightgoalpost :deserialize buf ptr-) (incf ptr- (send _rightgoalpost :serialization-length))
   ;;
   self)
  )

(setf (get vision_msgs::Webotsmsg :md5sum-) "2b9c0baf80135ab319a9a2d5f79a6c9a")
(setf (get vision_msgs::Webotsmsg :datatype-) "vision_msgs/Webotsmsg")
(setf (get vision_msgs::Webotsmsg :definition-)
      "bool searching
uint8 fps
vision_msgs/Ball ball
vision_msgs/Leftgoalpost leftgoalpost
vision_msgs/Rightgoalpost rightgoalpost
================================================================================
MSG: vision_msgs/Ball
bool found
int32 x
int32 y
int32 roi_width
int32 roi_height
================================================================================
MSG: vision_msgs/Leftgoalpost
bool found
int32 x
int32 y
int32 roi_width
int32 roi_height

================================================================================
MSG: vision_msgs/Rightgoalpost
bool found
int32 x
int32 y
int32 roi_width
int32 roi_height

")



(provide :vision_msgs/Webotsmsg "2b9c0baf80135ab319a9a2d5f79a6c9a")


