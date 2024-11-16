;; Auto-generated. Do not edit!


(when (boundp 'modularized_bhv_msgs::stateMachineMsg)
  (if (not (find-package "MODULARIZED_BHV_MSGS"))
    (make-package "MODULARIZED_BHV_MSGS"))
  (shadow 'stateMachineMsg (find-package "MODULARIZED_BHV_MSGS")))
(unless (find-package "MODULARIZED_BHV_MSGS::STATEMACHINEMSG")
  (make-package "MODULARIZED_BHV_MSGS::STATEMACHINEMSG"))

(in-package "ROS")
;;//! \htmlinclude stateMachineMsg.msg.html


(defclass modularized_bhv_msgs::stateMachineMsg
  :super ros::object
  :slots (_ballPosition _ballClose _ballFound _fallState _horMotorOutOfCenter _headKickCheck ))

(defmethod modularized_bhv_msgs::stateMachineMsg
  (:init
   (&key
    ((:ballPosition __ballPosition) "")
    ((:ballClose __ballClose) nil)
    ((:ballFound __ballFound) nil)
    ((:fallState __fallState) "")
    ((:horMotorOutOfCenter __horMotorOutOfCenter) "")
    ((:headKickCheck __headKickCheck) nil)
    )
   (send-super :init)
   (setq _ballPosition (string __ballPosition))
   (setq _ballClose __ballClose)
   (setq _ballFound __ballFound)
   (setq _fallState (string __fallState))
   (setq _horMotorOutOfCenter (string __horMotorOutOfCenter))
   (setq _headKickCheck __headKickCheck)
   self)
  (:ballPosition
   (&optional __ballPosition)
   (if __ballPosition (setq _ballPosition __ballPosition)) _ballPosition)
  (:ballClose
   (&optional (__ballClose :null))
   (if (not (eq __ballClose :null)) (setq _ballClose __ballClose)) _ballClose)
  (:ballFound
   (&optional (__ballFound :null))
   (if (not (eq __ballFound :null)) (setq _ballFound __ballFound)) _ballFound)
  (:fallState
   (&optional __fallState)
   (if __fallState (setq _fallState __fallState)) _fallState)
  (:horMotorOutOfCenter
   (&optional __horMotorOutOfCenter)
   (if __horMotorOutOfCenter (setq _horMotorOutOfCenter __horMotorOutOfCenter)) _horMotorOutOfCenter)
  (:headKickCheck
   (&optional (__headKickCheck :null))
   (if (not (eq __headKickCheck :null)) (setq _headKickCheck __headKickCheck)) _headKickCheck)
  (:serialization-length
   ()
   (+
    ;; string _ballPosition
    4 (length _ballPosition)
    ;; bool _ballClose
    1
    ;; bool _ballFound
    1
    ;; string _fallState
    4 (length _fallState)
    ;; string _horMotorOutOfCenter
    4 (length _horMotorOutOfCenter)
    ;; bool _headKickCheck
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _ballPosition
       (write-long (length _ballPosition) s) (princ _ballPosition s)
     ;; bool _ballClose
       (if _ballClose (write-byte -1 s) (write-byte 0 s))
     ;; bool _ballFound
       (if _ballFound (write-byte -1 s) (write-byte 0 s))
     ;; string _fallState
       (write-long (length _fallState) s) (princ _fallState s)
     ;; string _horMotorOutOfCenter
       (write-long (length _horMotorOutOfCenter) s) (princ _horMotorOutOfCenter s)
     ;; bool _headKickCheck
       (if _headKickCheck (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _ballPosition
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ballPosition (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _ballClose
     (setq _ballClose (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _ballFound
     (setq _ballFound (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _fallState
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _fallState (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _horMotorOutOfCenter
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _horMotorOutOfCenter (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _headKickCheck
     (setq _headKickCheck (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get modularized_bhv_msgs::stateMachineMsg :md5sum-) "c591d7d3c44206a23a253ed3e26e96da")
(setf (get modularized_bhv_msgs::stateMachineMsg :datatype-) "modularized_bhv_msgs/stateMachineMsg")
(setf (get modularized_bhv_msgs::stateMachineMsg :definition-)
      "string ballPosition
bool ballClose
bool ballFound
string fallState
string horMotorOutOfCenter
bool headKickCheck
")



(provide :modularized_bhv_msgs/stateMachineMsg "c591d7d3c44206a23a253ed3e26e96da")


