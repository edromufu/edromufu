;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::OpencmResponseMsg)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'OpencmResponseMsg (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::OPENCMRESPONSEMSG")
  (make-package "MOVEMENT_MSGS::OPENCMRESPONSEMSG"))

(in-package "ROS")
;;//! \htmlinclude OpencmResponseMsg.msg.html


(defclass movement_msgs::OpencmResponseMsg
  :super ros::object
  :slots (_motors_position _motors_velocity ))

(defmethod movement_msgs::OpencmResponseMsg
  (:init
   (&key
    ((:motors_position __motors_position) (make-array 20 :initial-element 0 :element-type :integer))
    ((:motors_velocity __motors_velocity) (make-array 20 :initial-element 0 :element-type :integer))
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
    ;; int16[20] _motors_position
    (* 2    20)
    ;; int16[20] _motors_velocity
    (* 2    20)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16[20] _motors_position
     (dotimes (i 20)
       (write-word (elt _motors_position i) s)
       )
     ;; int16[20] _motors_velocity
     (dotimes (i 20)
       (write-word (elt _motors_velocity i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16[20] _motors_position
   (dotimes (i (length _motors_position))
     (setf (elt _motors_position i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; int16[20] _motors_velocity
   (dotimes (i (length _motors_velocity))
     (setf (elt _motors_velocity i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;;
   self)
  )

(setf (get movement_msgs::OpencmResponseMsg :md5sum-) "f292bdc80699153415d4562d7f08a5e4")
(setf (get movement_msgs::OpencmResponseMsg :datatype-) "movement_msgs/OpencmResponseMsg")
(setf (get movement_msgs::OpencmResponseMsg :definition-)
      "int16[20] motors_position
int16[20] motors_velocity

")



(provide :movement_msgs/OpencmResponseMsg "f292bdc80699153415d4562d7f08a5e4")


