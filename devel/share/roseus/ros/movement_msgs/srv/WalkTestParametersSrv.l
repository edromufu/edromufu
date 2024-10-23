;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::WalkTestParametersSrv)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'WalkTestParametersSrv (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::WALKTESTPARAMETERSSRV")
  (make-package "MOVEMENT_MSGS::WALKTESTPARAMETERSSRV"))
(unless (find-package "MOVEMENT_MSGS::WALKTESTPARAMETERSSRVREQUEST")
  (make-package "MOVEMENT_MSGS::WALKTESTPARAMETERSSRVREQUEST"))
(unless (find-package "MOVEMENT_MSGS::WALKTESTPARAMETERSSRVRESPONSE")
  (make-package "MOVEMENT_MSGS::WALKTESTPARAMETERSSRVRESPONSE"))

(in-package "ROS")





(defclass movement_msgs::WalkTestParametersSrvRequest
  :super ros::object
  :slots (_currentWalk _stepGain _lateralGain _turnGain _freq _supportPhaseRatio _footYOffset _riseGain _trunkZOffset _swingGain _swingRollGain _swingPhase _stepUpVel _stepDownVel _riseUpVel _riseDownVel _swingPause _swingVel _trunkXOffset _trunkYOffset _trunkPitch _trunkRoll _extraLeftX _extraLeftY _extraLeftZ _extraRightX _extraRightY _extraRightZ _extraLeftYaw _extraLeftPitch _extraLeftRoll _extraRightYaw _extraRightPitch _extraRightRoll ))

(defmethod movement_msgs::WalkTestParametersSrvRequest
  (:init
   (&key
    ((:currentWalk __currentWalk) "")
    ((:stepGain __stepGain) 0.0)
    ((:lateralGain __lateralGain) 0.0)
    ((:turnGain __turnGain) 0.0)
    ((:freq __freq) 0.0)
    ((:supportPhaseRatio __supportPhaseRatio) 0.0)
    ((:footYOffset __footYOffset) 0.0)
    ((:riseGain __riseGain) 0.0)
    ((:trunkZOffset __trunkZOffset) 0.0)
    ((:swingGain __swingGain) 0.0)
    ((:swingRollGain __swingRollGain) 0.0)
    ((:swingPhase __swingPhase) 0.0)
    ((:stepUpVel __stepUpVel) 0.0)
    ((:stepDownVel __stepDownVel) 0.0)
    ((:riseUpVel __riseUpVel) 0.0)
    ((:riseDownVel __riseDownVel) 0.0)
    ((:swingPause __swingPause) 0.0)
    ((:swingVel __swingVel) 0.0)
    ((:trunkXOffset __trunkXOffset) 0.0)
    ((:trunkYOffset __trunkYOffset) 0.0)
    ((:trunkPitch __trunkPitch) 0.0)
    ((:trunkRoll __trunkRoll) 0.0)
    ((:extraLeftX __extraLeftX) 0.0)
    ((:extraLeftY __extraLeftY) 0.0)
    ((:extraLeftZ __extraLeftZ) 0.0)
    ((:extraRightX __extraRightX) 0.0)
    ((:extraRightY __extraRightY) 0.0)
    ((:extraRightZ __extraRightZ) 0.0)
    ((:extraLeftYaw __extraLeftYaw) 0.0)
    ((:extraLeftPitch __extraLeftPitch) 0.0)
    ((:extraLeftRoll __extraLeftRoll) 0.0)
    ((:extraRightYaw __extraRightYaw) 0.0)
    ((:extraRightPitch __extraRightPitch) 0.0)
    ((:extraRightRoll __extraRightRoll) 0.0)
    )
   (send-super :init)
   (setq _currentWalk (string __currentWalk))
   (setq _stepGain (float __stepGain))
   (setq _lateralGain (float __lateralGain))
   (setq _turnGain (float __turnGain))
   (setq _freq (float __freq))
   (setq _supportPhaseRatio (float __supportPhaseRatio))
   (setq _footYOffset (float __footYOffset))
   (setq _riseGain (float __riseGain))
   (setq _trunkZOffset (float __trunkZOffset))
   (setq _swingGain (float __swingGain))
   (setq _swingRollGain (float __swingRollGain))
   (setq _swingPhase (float __swingPhase))
   (setq _stepUpVel (float __stepUpVel))
   (setq _stepDownVel (float __stepDownVel))
   (setq _riseUpVel (float __riseUpVel))
   (setq _riseDownVel (float __riseDownVel))
   (setq _swingPause (float __swingPause))
   (setq _swingVel (float __swingVel))
   (setq _trunkXOffset (float __trunkXOffset))
   (setq _trunkYOffset (float __trunkYOffset))
   (setq _trunkPitch (float __trunkPitch))
   (setq _trunkRoll (float __trunkRoll))
   (setq _extraLeftX (float __extraLeftX))
   (setq _extraLeftY (float __extraLeftY))
   (setq _extraLeftZ (float __extraLeftZ))
   (setq _extraRightX (float __extraRightX))
   (setq _extraRightY (float __extraRightY))
   (setq _extraRightZ (float __extraRightZ))
   (setq _extraLeftYaw (float __extraLeftYaw))
   (setq _extraLeftPitch (float __extraLeftPitch))
   (setq _extraLeftRoll (float __extraLeftRoll))
   (setq _extraRightYaw (float __extraRightYaw))
   (setq _extraRightPitch (float __extraRightPitch))
   (setq _extraRightRoll (float __extraRightRoll))
   self)
  (:currentWalk
   (&optional __currentWalk)
   (if __currentWalk (setq _currentWalk __currentWalk)) _currentWalk)
  (:stepGain
   (&optional __stepGain)
   (if __stepGain (setq _stepGain __stepGain)) _stepGain)
  (:lateralGain
   (&optional __lateralGain)
   (if __lateralGain (setq _lateralGain __lateralGain)) _lateralGain)
  (:turnGain
   (&optional __turnGain)
   (if __turnGain (setq _turnGain __turnGain)) _turnGain)
  (:freq
   (&optional __freq)
   (if __freq (setq _freq __freq)) _freq)
  (:supportPhaseRatio
   (&optional __supportPhaseRatio)
   (if __supportPhaseRatio (setq _supportPhaseRatio __supportPhaseRatio)) _supportPhaseRatio)
  (:footYOffset
   (&optional __footYOffset)
   (if __footYOffset (setq _footYOffset __footYOffset)) _footYOffset)
  (:riseGain
   (&optional __riseGain)
   (if __riseGain (setq _riseGain __riseGain)) _riseGain)
  (:trunkZOffset
   (&optional __trunkZOffset)
   (if __trunkZOffset (setq _trunkZOffset __trunkZOffset)) _trunkZOffset)
  (:swingGain
   (&optional __swingGain)
   (if __swingGain (setq _swingGain __swingGain)) _swingGain)
  (:swingRollGain
   (&optional __swingRollGain)
   (if __swingRollGain (setq _swingRollGain __swingRollGain)) _swingRollGain)
  (:swingPhase
   (&optional __swingPhase)
   (if __swingPhase (setq _swingPhase __swingPhase)) _swingPhase)
  (:stepUpVel
   (&optional __stepUpVel)
   (if __stepUpVel (setq _stepUpVel __stepUpVel)) _stepUpVel)
  (:stepDownVel
   (&optional __stepDownVel)
   (if __stepDownVel (setq _stepDownVel __stepDownVel)) _stepDownVel)
  (:riseUpVel
   (&optional __riseUpVel)
   (if __riseUpVel (setq _riseUpVel __riseUpVel)) _riseUpVel)
  (:riseDownVel
   (&optional __riseDownVel)
   (if __riseDownVel (setq _riseDownVel __riseDownVel)) _riseDownVel)
  (:swingPause
   (&optional __swingPause)
   (if __swingPause (setq _swingPause __swingPause)) _swingPause)
  (:swingVel
   (&optional __swingVel)
   (if __swingVel (setq _swingVel __swingVel)) _swingVel)
  (:trunkXOffset
   (&optional __trunkXOffset)
   (if __trunkXOffset (setq _trunkXOffset __trunkXOffset)) _trunkXOffset)
  (:trunkYOffset
   (&optional __trunkYOffset)
   (if __trunkYOffset (setq _trunkYOffset __trunkYOffset)) _trunkYOffset)
  (:trunkPitch
   (&optional __trunkPitch)
   (if __trunkPitch (setq _trunkPitch __trunkPitch)) _trunkPitch)
  (:trunkRoll
   (&optional __trunkRoll)
   (if __trunkRoll (setq _trunkRoll __trunkRoll)) _trunkRoll)
  (:extraLeftX
   (&optional __extraLeftX)
   (if __extraLeftX (setq _extraLeftX __extraLeftX)) _extraLeftX)
  (:extraLeftY
   (&optional __extraLeftY)
   (if __extraLeftY (setq _extraLeftY __extraLeftY)) _extraLeftY)
  (:extraLeftZ
   (&optional __extraLeftZ)
   (if __extraLeftZ (setq _extraLeftZ __extraLeftZ)) _extraLeftZ)
  (:extraRightX
   (&optional __extraRightX)
   (if __extraRightX (setq _extraRightX __extraRightX)) _extraRightX)
  (:extraRightY
   (&optional __extraRightY)
   (if __extraRightY (setq _extraRightY __extraRightY)) _extraRightY)
  (:extraRightZ
   (&optional __extraRightZ)
   (if __extraRightZ (setq _extraRightZ __extraRightZ)) _extraRightZ)
  (:extraLeftYaw
   (&optional __extraLeftYaw)
   (if __extraLeftYaw (setq _extraLeftYaw __extraLeftYaw)) _extraLeftYaw)
  (:extraLeftPitch
   (&optional __extraLeftPitch)
   (if __extraLeftPitch (setq _extraLeftPitch __extraLeftPitch)) _extraLeftPitch)
  (:extraLeftRoll
   (&optional __extraLeftRoll)
   (if __extraLeftRoll (setq _extraLeftRoll __extraLeftRoll)) _extraLeftRoll)
  (:extraRightYaw
   (&optional __extraRightYaw)
   (if __extraRightYaw (setq _extraRightYaw __extraRightYaw)) _extraRightYaw)
  (:extraRightPitch
   (&optional __extraRightPitch)
   (if __extraRightPitch (setq _extraRightPitch __extraRightPitch)) _extraRightPitch)
  (:extraRightRoll
   (&optional __extraRightRoll)
   (if __extraRightRoll (setq _extraRightRoll __extraRightRoll)) _extraRightRoll)
  (:serialization-length
   ()
   (+
    ;; string _currentWalk
    4 (length _currentWalk)
    ;; float64 _stepGain
    8
    ;; float64 _lateralGain
    8
    ;; float64 _turnGain
    8
    ;; float64 _freq
    8
    ;; float64 _supportPhaseRatio
    8
    ;; float64 _footYOffset
    8
    ;; float64 _riseGain
    8
    ;; float64 _trunkZOffset
    8
    ;; float64 _swingGain
    8
    ;; float64 _swingRollGain
    8
    ;; float64 _swingPhase
    8
    ;; float64 _stepUpVel
    8
    ;; float64 _stepDownVel
    8
    ;; float64 _riseUpVel
    8
    ;; float64 _riseDownVel
    8
    ;; float64 _swingPause
    8
    ;; float64 _swingVel
    8
    ;; float64 _trunkXOffset
    8
    ;; float64 _trunkYOffset
    8
    ;; float64 _trunkPitch
    8
    ;; float64 _trunkRoll
    8
    ;; float64 _extraLeftX
    8
    ;; float64 _extraLeftY
    8
    ;; float64 _extraLeftZ
    8
    ;; float64 _extraRightX
    8
    ;; float64 _extraRightY
    8
    ;; float64 _extraRightZ
    8
    ;; float64 _extraLeftYaw
    8
    ;; float64 _extraLeftPitch
    8
    ;; float64 _extraLeftRoll
    8
    ;; float64 _extraRightYaw
    8
    ;; float64 _extraRightPitch
    8
    ;; float64 _extraRightRoll
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _currentWalk
       (write-long (length _currentWalk) s) (princ _currentWalk s)
     ;; float64 _stepGain
       (sys::poke _stepGain (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _lateralGain
       (sys::poke _lateralGain (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _turnGain
       (sys::poke _turnGain (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _freq
       (sys::poke _freq (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _supportPhaseRatio
       (sys::poke _supportPhaseRatio (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _footYOffset
       (sys::poke _footYOffset (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _riseGain
       (sys::poke _riseGain (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trunkZOffset
       (sys::poke _trunkZOffset (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _swingGain
       (sys::poke _swingGain (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _swingRollGain
       (sys::poke _swingRollGain (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _swingPhase
       (sys::poke _swingPhase (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _stepUpVel
       (sys::poke _stepUpVel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _stepDownVel
       (sys::poke _stepDownVel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _riseUpVel
       (sys::poke _riseUpVel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _riseDownVel
       (sys::poke _riseDownVel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _swingPause
       (sys::poke _swingPause (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _swingVel
       (sys::poke _swingVel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trunkXOffset
       (sys::poke _trunkXOffset (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trunkYOffset
       (sys::poke _trunkYOffset (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trunkPitch
       (sys::poke _trunkPitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trunkRoll
       (sys::poke _trunkRoll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraLeftX
       (sys::poke _extraLeftX (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraLeftY
       (sys::poke _extraLeftY (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraLeftZ
       (sys::poke _extraLeftZ (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraRightX
       (sys::poke _extraRightX (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraRightY
       (sys::poke _extraRightY (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraRightZ
       (sys::poke _extraRightZ (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraLeftYaw
       (sys::poke _extraLeftYaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraLeftPitch
       (sys::poke _extraLeftPitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraLeftRoll
       (sys::poke _extraLeftRoll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraRightYaw
       (sys::poke _extraRightYaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraRightPitch
       (sys::poke _extraRightPitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _extraRightRoll
       (sys::poke _extraRightRoll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _currentWalk
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _currentWalk (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _stepGain
     (setq _stepGain (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _lateralGain
     (setq _lateralGain (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _turnGain
     (setq _turnGain (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _freq
     (setq _freq (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _supportPhaseRatio
     (setq _supportPhaseRatio (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _footYOffset
     (setq _footYOffset (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _riseGain
     (setq _riseGain (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trunkZOffset
     (setq _trunkZOffset (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _swingGain
     (setq _swingGain (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _swingRollGain
     (setq _swingRollGain (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _swingPhase
     (setq _swingPhase (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _stepUpVel
     (setq _stepUpVel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _stepDownVel
     (setq _stepDownVel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _riseUpVel
     (setq _riseUpVel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _riseDownVel
     (setq _riseDownVel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _swingPause
     (setq _swingPause (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _swingVel
     (setq _swingVel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trunkXOffset
     (setq _trunkXOffset (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trunkYOffset
     (setq _trunkYOffset (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trunkPitch
     (setq _trunkPitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trunkRoll
     (setq _trunkRoll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraLeftX
     (setq _extraLeftX (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraLeftY
     (setq _extraLeftY (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraLeftZ
     (setq _extraLeftZ (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraRightX
     (setq _extraRightX (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraRightY
     (setq _extraRightY (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraRightZ
     (setq _extraRightZ (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraLeftYaw
     (setq _extraLeftYaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraLeftPitch
     (setq _extraLeftPitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraLeftRoll
     (setq _extraLeftRoll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraRightYaw
     (setq _extraRightYaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraRightPitch
     (setq _extraRightPitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _extraRightRoll
     (setq _extraRightRoll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass movement_msgs::WalkTestParametersSrvResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_msgs::WalkTestParametersSrvResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass movement_msgs::WalkTestParametersSrv
  :super ros::object
  :slots ())

(setf (get movement_msgs::WalkTestParametersSrv :md5sum-) "7113a794fe0bdf7ad1da5428852cd6a2")
(setf (get movement_msgs::WalkTestParametersSrv :datatype-) "movement_msgs/WalkTestParametersSrv")
(setf (get movement_msgs::WalkTestParametersSrv :request) movement_msgs::WalkTestParametersSrvRequest)
(setf (get movement_msgs::WalkTestParametersSrv :response) movement_msgs::WalkTestParametersSrvResponse)

(defmethod movement_msgs::WalkTestParametersSrvRequest
  (:response () (instance movement_msgs::WalkTestParametersSrvResponse :init)))

(setf (get movement_msgs::WalkTestParametersSrvRequest :md5sum-) "7113a794fe0bdf7ad1da5428852cd6a2")
(setf (get movement_msgs::WalkTestParametersSrvRequest :datatype-) "movement_msgs/WalkTestParametersSrvRequest")
(setf (get movement_msgs::WalkTestParametersSrvRequest :definition-)
      "string currentWalk
float64 stepGain
float64 lateralGain
float64 turnGain
float64 freq
float64 supportPhaseRatio
float64 footYOffset
float64 riseGain
float64 trunkZOffset
float64 swingGain
float64 swingRollGain
float64 swingPhase
float64 stepUpVel
float64 stepDownVel
float64 riseUpVel
float64 riseDownVel
float64 swingPause
float64 swingVel
float64 trunkXOffset
float64 trunkYOffset
float64 trunkPitch
float64 trunkRoll
float64 extraLeftX
float64 extraLeftY
float64 extraLeftZ
float64 extraRightX
float64 extraRightY
float64 extraRightZ
float64 extraLeftYaw
float64 extraLeftPitch
float64 extraLeftRoll
float64 extraRightYaw
float64 extraRightPitch
float64 extraRightRoll

---

bool success
")

(setf (get movement_msgs::WalkTestParametersSrvResponse :md5sum-) "7113a794fe0bdf7ad1da5428852cd6a2")
(setf (get movement_msgs::WalkTestParametersSrvResponse :datatype-) "movement_msgs/WalkTestParametersSrvResponse")
(setf (get movement_msgs::WalkTestParametersSrvResponse :definition-)
      "string currentWalk
float64 stepGain
float64 lateralGain
float64 turnGain
float64 freq
float64 supportPhaseRatio
float64 footYOffset
float64 riseGain
float64 trunkZOffset
float64 swingGain
float64 swingRollGain
float64 swingPhase
float64 stepUpVel
float64 stepDownVel
float64 riseUpVel
float64 riseDownVel
float64 swingPause
float64 swingVel
float64 trunkXOffset
float64 trunkYOffset
float64 trunkPitch
float64 trunkRoll
float64 extraLeftX
float64 extraLeftY
float64 extraLeftZ
float64 extraRightX
float64 extraRightY
float64 extraRightZ
float64 extraLeftYaw
float64 extraLeftPitch
float64 extraLeftRoll
float64 extraRightYaw
float64 extraRightPitch
float64 extraRightRoll

---

bool success
")



(provide :movement_msgs/WalkTestParametersSrv "7113a794fe0bdf7ad1da5428852cd6a2")


