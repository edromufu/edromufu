;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::ApprovedMovementMsg)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'ApprovedMovementMsg (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::APPROVEDMOVEMENTMSG")
  (make-package "MOVEMENT_MSGS::APPROVEDMOVEMENTMSG"))

(in-package "ROS")
;;//! \htmlinclude ApprovedMovementMsg.msg.html


(defclass movement_msgs::ApprovedMovementMsg
  :super ros::object
  :slots (_approved_movement ))

(defmethod movement_msgs::ApprovedMovementMsg
  (:init
   (&key
    ((:approved_movement __approved_movement) "")
    )
   (send-super :init)
   (setq _approved_movement (string __approved_movement))
   self)
  (:approved_movement
   (&optional __approved_movement)
   (if __approved_movement (setq _approved_movement __approved_movement)) _approved_movement)
  (:serialization-length
   ()
   (+
    ;; string _approved_movement
    4 (length _approved_movement)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _approved_movement
       (write-long (length _approved_movement) s) (princ _approved_movement s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _approved_movement
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _approved_movement (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get movement_msgs::ApprovedMovementMsg :md5sum-) "255fbce3bb4374d8b5382cbf8e9f1840")
(setf (get movement_msgs::ApprovedMovementMsg :datatype-) "movement_msgs/ApprovedMovementMsg")
(setf (get movement_msgs::ApprovedMovementMsg :definition-)
      "string approved_movement


")



(provide :movement_msgs/ApprovedMovementMsg "255fbce3bb4374d8b5382cbf8e9f1840")


