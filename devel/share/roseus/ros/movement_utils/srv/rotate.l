;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::rotate)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'rotate (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::ROTATE")
  (make-package "MOVEMENT_UTILS::ROTATE"))
(unless (find-package "MOVEMENT_UTILS::ROTATEREQUEST")
  (make-package "MOVEMENT_UTILS::ROTATEREQUEST"))
(unless (find-package "MOVEMENT_UTILS::ROTATERESPONSE")
  (make-package "MOVEMENT_UTILS::ROTATERESPONSE"))

(in-package "ROS")





(defclass movement_utils::rotateRequest
  :super ros::object
  :slots (_direction _steps_number ))

(defmethod movement_utils::rotateRequest
  (:init
   (&key
    ((:direction __direction) 0)
    ((:steps_number __steps_number) 0)
    )
   (send-super :init)
   (setq _direction (round __direction))
   (setq _steps_number (round __steps_number))
   self)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:steps_number
   (&optional __steps_number)
   (if __steps_number (setq _steps_number __steps_number)) _steps_number)
  (:serialization-length
   ()
   (+
    ;; int8 _direction
    1
    ;; int8 _steps_number
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _direction
       (write-byte _direction s)
     ;; int8 _steps_number
       (write-byte _steps_number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _direction
     (setq _direction (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _direction 127) (setq _direction (- _direction 256)))
   ;; int8 _steps_number
     (setq _steps_number (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _steps_number 127) (setq _steps_number (- _steps_number 256)))
   ;;
   self)
  )

(defclass movement_utils::rotateResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::rotateResponse
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

(defclass movement_utils::rotate
  :super ros::object
  :slots ())

(setf (get movement_utils::rotate :md5sum-) "4589fa56bf3a1c197ab709f13c7adc75")
(setf (get movement_utils::rotate :datatype-) "movement_utils/rotate")
(setf (get movement_utils::rotate :request) movement_utils::rotateRequest)
(setf (get movement_utils::rotate :response) movement_utils::rotateResponse)

(defmethod movement_utils::rotateRequest
  (:response () (instance movement_utils::rotateResponse :init)))

(setf (get movement_utils::rotateRequest :md5sum-) "4589fa56bf3a1c197ab709f13c7adc75")
(setf (get movement_utils::rotateRequest :datatype-) "movement_utils/rotateRequest")
(setf (get movement_utils::rotateRequest :definition-)
      "int8 direction
int8 steps_number
---
bool success
")

(setf (get movement_utils::rotateResponse :md5sum-) "4589fa56bf3a1c197ab709f13c7adc75")
(setf (get movement_utils::rotateResponse :datatype-) "movement_utils/rotateResponse")
(setf (get movement_utils::rotateResponse :definition-)
      "int8 direction
int8 steps_number
---
bool success
")



(provide :movement_utils/rotate "4589fa56bf3a1c197ab709f13c7adc75")


