;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::WebotsRequestMsg)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'WebotsRequestMsg (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::WEBOTSREQUESTMSG")
  (make-package "MOVEMENT_MSGS::WEBOTSREQUESTMSG"))

(in-package "ROS")
;;//! \htmlinclude WebotsRequestMsg.msg.html


(defclass movement_msgs::WebotsRequestMsg
  :super ros::object
  :slots (_motors_position _motors_velocity ))

(defmethod movement_msgs::WebotsRequestMsg
  (:init
   (&key
    ((:motors_position __motors_position) (make-array 20 :initial-element 0.0 :element-type :float))
    ((:motors_velocity __motors_velocity) (make-array 20 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _motors_position __motors_position)
   (setq _motors_velocity __motors_velocity)
   self)
  (:motors_position
   (&optional __motors_position)
   (if __motors_position (setq _motors_position __motors_position)) _motors_position)
  (:motors_velocity
   (&optional __motors_velocity)
   (if __motors_velocity (setq _motors_velocity __motors_velocity)) _motors_velocity)
  (:serialization-length
   ()
   (+
    ;; float32[20] _motors_position
    (* 4    20)
    ;; float32[20] _motors_velocity
    (* 4    20)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[20] _motors_position
     (dotimes (i 20)
       (sys::poke (elt _motors_position i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[20] _motors_velocity
     (dotimes (i 20)
       (sys::poke (elt _motors_velocity i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[20] _motors_position
   (dotimes (i (length _motors_position))
     (setf (elt _motors_position i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32[20] _motors_velocity
   (dotimes (i (length _motors_velocity))
     (setf (elt _motors_velocity i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get movement_msgs::WebotsRequestMsg :md5sum-) "3463d5e3ddb49315fab6bfa4cde9cb44")
(setf (get movement_msgs::WebotsRequestMsg :datatype-) "movement_msgs/WebotsRequestMsg")
(setf (get movement_msgs::WebotsRequestMsg :definition-)
      "float32[20] motors_position
float32[20] motors_velocity
")



(provide :movement_msgs/WebotsRequestMsg "3463d5e3ddb49315fab6bfa4cde9cb44")


