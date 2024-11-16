;; Auto-generated. Do not edit!


(when (boundp 'modularized_bhv_msgs::currentStateMsg)
  (if (not (find-package "MODULARIZED_BHV_MSGS"))
    (make-package "MODULARIZED_BHV_MSGS"))
  (shadow 'currentStateMsg (find-package "MODULARIZED_BHV_MSGS")))
(unless (find-package "MODULARIZED_BHV_MSGS::CURRENTSTATEMSG")
  (make-package "MODULARIZED_BHV_MSGS::CURRENTSTATEMSG"))

(in-package "ROS")
;;//! \htmlinclude currentStateMsg.msg.html


(defclass modularized_bhv_msgs::currentStateMsg
  :super ros::object
  :slots (_currentState ))

(defmethod modularized_bhv_msgs::currentStateMsg
  (:init
   (&key
    ((:currentState __currentState) "")
    )
   (send-super :init)
   (setq _currentState (string __currentState))
   self)
  (:currentState
   (&optional __currentState)
   (if __currentState (setq _currentState __currentState)) _currentState)
  (:serialization-length
   ()
   (+
    ;; string _currentState
    4 (length _currentState)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _currentState
       (write-long (length _currentState) s) (princ _currentState s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _currentState
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _currentState (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get modularized_bhv_msgs::currentStateMsg :md5sum-) "51b88f6d6df0913c6465fdbbb69a8c4e")
(setf (get modularized_bhv_msgs::currentStateMsg :datatype-) "modularized_bhv_msgs/currentStateMsg")
(setf (get modularized_bhv_msgs::currentStateMsg :definition-)
      "string currentState
")



(provide :modularized_bhv_msgs/currentStateMsg "51b88f6d6df0913c6465fdbbb69a8c4e")


