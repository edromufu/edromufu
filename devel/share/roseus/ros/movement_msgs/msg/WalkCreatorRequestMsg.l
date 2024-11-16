;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::WalkCreatorRequestMsg)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'WalkCreatorRequestMsg (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::WALKCREATORREQUESTMSG")
  (make-package "MOVEMENT_MSGS::WALKCREATORREQUESTMSG"))

(in-package "ROS")
;;//! \htmlinclude WalkCreatorRequestMsg.msg.html


(defclass movement_msgs::WalkCreatorRequestMsg
  :super ros::object
  :slots (_enabledGain _stepGain _lateralGain _turnGain ))

(defmethod movement_msgs::WalkCreatorRequestMsg
  (:init
   (&key
    ((:enabledGain __enabledGain) nil)
    ((:stepGain __stepGain) 0.0)
    ((:lateralGain __lateralGain) 0.0)
    ((:turnGain __turnGain) 0.0)
    )
   (send-super :init)
   (setq _enabledGain __enabledGain)
   (setq _stepGain (float __stepGain))
   (setq _lateralGain (float __lateralGain))
   (setq _turnGain (float __turnGain))
   self)
  (:enabledGain
   (&optional (__enabledGain :null))
   (if (not (eq __enabledGain :null)) (setq _enabledGain __enabledGain)) _enabledGain)
  (:stepGain
   (&optional __stepGain)
   (if __stepGain (setq _stepGain __stepGain)) _stepGain)
  (:lateralGain
   (&optional __lateralGain)
   (if __lateralGain (setq _lateralGain __lateralGain)) _lateralGain)
  (:turnGain
   (&optional __turnGain)
   (if __turnGain (setq _turnGain __turnGain)) _turnGain)
  (:serialization-length
   ()
   (+
    ;; bool _enabledGain
    1
    ;; float32 _stepGain
    4
    ;; float32 _lateralGain
    4
    ;; float32 _turnGain
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _enabledGain
       (if _enabledGain (write-byte -1 s) (write-byte 0 s))
     ;; float32 _stepGain
       (sys::poke _stepGain (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _lateralGain
       (sys::poke _lateralGain (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _turnGain
       (sys::poke _turnGain (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _enabledGain
     (setq _enabledGain (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _stepGain
     (setq _stepGain (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _lateralGain
     (setq _lateralGain (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _turnGain
     (setq _turnGain (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get movement_msgs::WalkCreatorRequestMsg :md5sum-) "9b4b735c8495180479cdcb415b06f8d4")
(setf (get movement_msgs::WalkCreatorRequestMsg :datatype-) "movement_msgs/WalkCreatorRequestMsg")
(setf (get movement_msgs::WalkCreatorRequestMsg :definition-)
      "bool   enabledGain
float32 stepGain
float32 lateralGain
float32 turnGain
")



(provide :movement_msgs/WalkCreatorRequestMsg "9b4b735c8495180479cdcb415b06f8d4")


