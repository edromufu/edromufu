;; Auto-generated. Do not edit!


(when (boundp 'vision_msgs::Leftgoalpost)
  (if (not (find-package "VISION_MSGS"))
    (make-package "VISION_MSGS"))
  (shadow 'Leftgoalpost (find-package "VISION_MSGS")))
(unless (find-package "VISION_MSGS::LEFTGOALPOST")
  (make-package "VISION_MSGS::LEFTGOALPOST"))

(in-package "ROS")
;;//! \htmlinclude Leftgoalpost.msg.html


(defclass vision_msgs::Leftgoalpost
  :super ros::object
  :slots (_found _x _y _roi_width _roi_height ))

(defmethod vision_msgs::Leftgoalpost
  (:init
   (&key
    ((:found __found) nil)
    ((:x __x) 0)
    ((:y __y) 0)
    ((:roi_width __roi_width) 0)
    ((:roi_height __roi_height) 0)
    )
   (send-super :init)
   (setq _found __found)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _roi_width (round __roi_width))
   (setq _roi_height (round __roi_height))
   self)
  (:found
   (&optional (__found :null))
   (if (not (eq __found :null)) (setq _found __found)) _found)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:roi_width
   (&optional __roi_width)
   (if __roi_width (setq _roi_width __roi_width)) _roi_width)
  (:roi_height
   (&optional __roi_height)
   (if __roi_height (setq _roi_height __roi_height)) _roi_height)
  (:serialization-length
   ()
   (+
    ;; bool _found
    1
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; int32 _roi_width
    4
    ;; int32 _roi_height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _found
       (if _found (write-byte -1 s) (write-byte 0 s))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; int32 _roi_width
       (write-long _roi_width s)
     ;; int32 _roi_height
       (write-long _roi_height s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _found
     (setq _found (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _roi_width
     (setq _roi_width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _roi_height
     (setq _roi_height (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get vision_msgs::Leftgoalpost :md5sum-) "593e6a8c66231b4fe6d1d33cf452902c")
(setf (get vision_msgs::Leftgoalpost :datatype-) "vision_msgs/Leftgoalpost")
(setf (get vision_msgs::Leftgoalpost :definition-)
      "bool found
int32 x
int32 y
int32 roi_width
int32 roi_height

")



(provide :vision_msgs/Leftgoalpost "593e6a8c66231b4fe6d1d33cf452902c")


