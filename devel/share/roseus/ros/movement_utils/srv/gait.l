;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::gait)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'gait (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::GAIT")
  (make-package "MOVEMENT_UTILS::GAIT"))
(unless (find-package "MOVEMENT_UTILS::GAITREQUEST")
  (make-package "MOVEMENT_UTILS::GAITREQUEST"))
(unless (find-package "MOVEMENT_UTILS::GAITRESPONSE")
  (make-package "MOVEMENT_UTILS::GAITRESPONSE"))

(in-package "ROS")





(defclass movement_utils::gaitRequest
  :super ros::object
  :slots (_steps_number _step_height ))

(defmethod movement_utils::gaitRequest
  (:init
   (&key
    ((:steps_number __steps_number) 0)
    ((:step_height __step_height) 0.0)
    )
   (send-super :init)
   (setq _steps_number (round __steps_number))
   (setq _step_height (float __step_height))
   self)
  (:steps_number
   (&optional __steps_number)
   (if __steps_number (setq _steps_number __steps_number)) _steps_number)
  (:step_height
   (&optional __step_height)
   (if __step_height (setq _step_height __step_height)) _step_height)
  (:serialization-length
   ()
   (+
    ;; int8 _steps_number
    1
    ;; float32 _step_height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _steps_number
       (write-byte _steps_number s)
     ;; float32 _step_height
       (sys::poke _step_height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _steps_number
     (setq _steps_number (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _steps_number 127) (setq _steps_number (- _steps_number 256)))
   ;; float32 _step_height
     (setq _step_height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass movement_utils::gaitResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::gaitResponse
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

(defclass movement_utils::gait
  :super ros::object
  :slots ())

(setf (get movement_utils::gait :md5sum-) "372f208eec6910dde42b51ee38202481")
(setf (get movement_utils::gait :datatype-) "movement_utils/gait")
(setf (get movement_utils::gait :request) movement_utils::gaitRequest)
(setf (get movement_utils::gait :response) movement_utils::gaitResponse)

(defmethod movement_utils::gaitRequest
  (:response () (instance movement_utils::gaitResponse :init)))

(setf (get movement_utils::gaitRequest :md5sum-) "372f208eec6910dde42b51ee38202481")
(setf (get movement_utils::gaitRequest :datatype-) "movement_utils/gaitRequest")
(setf (get movement_utils::gaitRequest :definition-)
      "int8 steps_number
float32 step_height
---
bool success
")

(setf (get movement_utils::gaitResponse :md5sum-) "372f208eec6910dde42b51ee38202481")
(setf (get movement_utils::gaitResponse :datatype-) "movement_utils/gaitResponse")
(setf (get movement_utils::gaitResponse :definition-)
      "int8 steps_number
float32 step_height
---
bool success
")



(provide :movement_utils/gait "372f208eec6910dde42b51ee38202481")


