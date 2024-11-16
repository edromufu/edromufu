;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::HeadParamsMsg)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'HeadParamsMsg (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::HEADPARAMSMSG")
  (make-package "MOVEMENT_MSGS::HEADPARAMSMSG"))

(in-package "ROS")
;;//! \htmlinclude HeadParamsMsg.msg.html


(defclass movement_msgs::HeadParamsMsg
  :super ros::object
  :slots (_direction _pattern ))

(defmethod movement_msgs::HeadParamsMsg
  (:init
   (&key
    ((:direction __direction) "")
    ((:pattern __pattern) "")
    )
   (send-super :init)
   (setq _direction (string __direction))
   (setq _pattern (string __pattern))
   self)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:pattern
   (&optional __pattern)
   (if __pattern (setq _pattern __pattern)) _pattern)
  (:serialization-length
   ()
   (+
    ;; string _direction
    4 (length _direction)
    ;; string _pattern
    4 (length _pattern)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _direction
       (write-long (length _direction) s) (princ _direction s)
     ;; string _pattern
       (write-long (length _pattern) s) (princ _pattern s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _direction
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _direction (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _pattern
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _pattern (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get movement_msgs::HeadParamsMsg :md5sum-) "bd8add9ae07028e68b98196268fea8b1")
(setf (get movement_msgs::HeadParamsMsg :datatype-) "movement_msgs/HeadParamsMsg")
(setf (get movement_msgs::HeadParamsMsg :definition-)
      "string direction
string pattern
")



(provide :movement_msgs/HeadParamsMsg "bd8add9ae07028e68b98196268fea8b1")


