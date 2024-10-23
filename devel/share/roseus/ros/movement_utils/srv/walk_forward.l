;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::walk_forward)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'walk_forward (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::WALK_FORWARD")
  (make-package "MOVEMENT_UTILS::WALK_FORWARD"))
(unless (find-package "MOVEMENT_UTILS::WALK_FORWARDREQUEST")
  (make-package "MOVEMENT_UTILS::WALK_FORWARDREQUEST"))
(unless (find-package "MOVEMENT_UTILS::WALK_FORWARDRESPONSE")
  (make-package "MOVEMENT_UTILS::WALK_FORWARDRESPONSE"))

(in-package "ROS")





(defclass movement_utils::walk_forwardRequest
  :super ros::object
  :slots (_support_foot _steps_number ))

(defmethod movement_utils::walk_forwardRequest
  (:init
   (&key
    ((:support_foot __support_foot) 0)
    ((:steps_number __steps_number) 0)
    )
   (send-super :init)
   (setq _support_foot (round __support_foot))
   (setq _steps_number (round __steps_number))
   self)
  (:support_foot
   (&optional __support_foot)
   (if __support_foot (setq _support_foot __support_foot)) _support_foot)
  (:steps_number
   (&optional __steps_number)
   (if __steps_number (setq _steps_number __steps_number)) _steps_number)
  (:serialization-length
   ()
   (+
    ;; int8 _support_foot
    1
    ;; int8 _steps_number
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _support_foot
       (write-byte _support_foot s)
     ;; int8 _steps_number
       (write-byte _steps_number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _support_foot
     (setq _support_foot (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _support_foot 127) (setq _support_foot (- _support_foot 256)))
   ;; int8 _steps_number
     (setq _steps_number (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _steps_number 127) (setq _steps_number (- _steps_number 256)))
   ;;
   self)
  )

(defclass movement_utils::walk_forwardResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::walk_forwardResponse
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

(defclass movement_utils::walk_forward
  :super ros::object
  :slots ())

(setf (get movement_utils::walk_forward :md5sum-) "4e96d691545ef71c6c6ffe49fb624ea4")
(setf (get movement_utils::walk_forward :datatype-) "movement_utils/walk_forward")
(setf (get movement_utils::walk_forward :request) movement_utils::walk_forwardRequest)
(setf (get movement_utils::walk_forward :response) movement_utils::walk_forwardResponse)

(defmethod movement_utils::walk_forwardRequest
  (:response () (instance movement_utils::walk_forwardResponse :init)))

(setf (get movement_utils::walk_forwardRequest :md5sum-) "4e96d691545ef71c6c6ffe49fb624ea4")
(setf (get movement_utils::walk_forwardRequest :datatype-) "movement_utils/walk_forwardRequest")
(setf (get movement_utils::walk_forwardRequest :definition-)
      "int8 support_foot
int8 steps_number
---
bool success
")

(setf (get movement_utils::walk_forwardResponse :md5sum-) "4e96d691545ef71c6c6ffe49fb624ea4")
(setf (get movement_utils::walk_forwardResponse :datatype-) "movement_utils/walk_forwardResponse")
(setf (get movement_utils::walk_forwardResponse :definition-)
      "int8 support_foot
int8 steps_number
---
bool success
")



(provide :movement_utils/walk_forward "4e96d691545ef71c6c6ffe49fb624ea4")


