;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::WalkingPositionsMsg)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'WalkingPositionsMsg (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::WALKINGPOSITIONSMSG")
  (make-package "MOVEMENT_MSGS::WALKINGPOSITIONSMSG"))

(in-package "ROS")
;;//! \htmlinclude WalkingPositionsMsg.msg.html


(defclass movement_msgs::WalkingPositionsMsg
  :super ros::object
  :slots (_positions ))

(defmethod movement_msgs::WalkingPositionsMsg
  (:init
   (&key
    ((:positions __positions) (make-array 12 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _positions __positions)
   self)
  (:positions
   (&optional __positions)
   (if __positions (setq _positions __positions)) _positions)
  (:serialization-length
   ()
   (+
    ;; float64[12] _positions
    (* 8    12)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[12] _positions
     (dotimes (i 12)
       (sys::poke (elt _positions i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[12] _positions
   (dotimes (i (length _positions))
     (setf (elt _positions i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get movement_msgs::WalkingPositionsMsg :md5sum-) "432ba4694a7ccfad78b66057edbee5ed")
(setf (get movement_msgs::WalkingPositionsMsg :datatype-) "movement_msgs/WalkingPositionsMsg")
(setf (get movement_msgs::WalkingPositionsMsg :definition-)
      "float64[12] positions
")



(provide :movement_msgs/WalkingPositionsMsg "432ba4694a7ccfad78b66057edbee5ed")


