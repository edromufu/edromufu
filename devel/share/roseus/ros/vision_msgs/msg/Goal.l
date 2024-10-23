;; Auto-generated. Do not edit!


(when (boundp 'vision_msgs::Goal)
  (if (not (find-package "VISION_MSGS"))
    (make-package "VISION_MSGS"))
  (shadow 'Goal (find-package "VISION_MSGS")))
(unless (find-package "VISION_MSGS::GOAL")
  (make-package "VISION_MSGS::GOAL"))

(in-package "ROS")
;;//! \htmlinclude Goal.msg.html


(defclass vision_msgs::Goal
  :super ros::object
  :slots (_found _x _y ))

(defmethod vision_msgs::Goal
  (:init
   (&key
    ((:found __found) nil)
    ((:x __x) 0)
    ((:y __y) 0)
    )
   (send-super :init)
   (setq _found __found)
   (setq _x (round __x))
   (setq _y (round __y))
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
  (:serialization-length
   ()
   (+
    ;; bool _found
    1
    ;; int32 _x
    4
    ;; int32 _y
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
   ;;
   self)
  )

(setf (get vision_msgs::Goal :md5sum-) "3ecc742cf8f7a902df729f553275ba64")
(setf (get vision_msgs::Goal :datatype-) "vision_msgs/Goal")
(setf (get vision_msgs::Goal :definition-)
      "bool found
int32 x
int32 y
")



(provide :vision_msgs/Goal "3ecc742cf8f7a902df729f553275ba64")


