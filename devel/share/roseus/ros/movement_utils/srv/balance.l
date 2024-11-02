;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::balance)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'balance (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::BALANCE")
  (make-package "MOVEMENT_UTILS::BALANCE"))
(unless (find-package "MOVEMENT_UTILS::BALANCEREQUEST")
  (make-package "MOVEMENT_UTILS::BALANCEREQUEST"))
(unless (find-package "MOVEMENT_UTILS::BALANCERESPONSE")
  (make-package "MOVEMENT_UTILS::BALANCERESPONSE"))

(in-package "ROS")





(defclass movement_utils::balanceRequest
  :super ros::object
  :slots (_supported_foot ))

(defmethod movement_utils::balanceRequest
  (:init
   (&key
    ((:supported_foot __supported_foot) 0)
    )
   (send-super :init)
   (setq _supported_foot (round __supported_foot))
   self)
  (:supported_foot
   (&optional __supported_foot)
   (if __supported_foot (setq _supported_foot __supported_foot)) _supported_foot)
  (:serialization-length
   ()
   (+
    ;; int8 _supported_foot
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _supported_foot
       (write-byte _supported_foot s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _supported_foot
     (setq _supported_foot (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _supported_foot 127) (setq _supported_foot (- _supported_foot 256)))
   ;;
   self)
  )

(defclass movement_utils::balanceResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::balanceResponse
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

(defclass movement_utils::balance
  :super ros::object
  :slots ())

(setf (get movement_utils::balance :md5sum-) "01c548ad4bcd6f9d88f95b8adc185129")
(setf (get movement_utils::balance :datatype-) "movement_utils/balance")
(setf (get movement_utils::balance :request) movement_utils::balanceRequest)
(setf (get movement_utils::balance :response) movement_utils::balanceResponse)

(defmethod movement_utils::balanceRequest
  (:response () (instance movement_utils::balanceResponse :init)))

(setf (get movement_utils::balanceRequest :md5sum-) "01c548ad4bcd6f9d88f95b8adc185129")
(setf (get movement_utils::balanceRequest :datatype-) "movement_utils/balanceRequest")
(setf (get movement_utils::balanceRequest :definition-)
      "int8 supported_foot

---
bool success
")

(setf (get movement_utils::balanceResponse :md5sum-) "01c548ad4bcd6f9d88f95b8adc185129")
(setf (get movement_utils::balanceResponse :datatype-) "movement_utils/balanceResponse")
(setf (get movement_utils::balanceResponse :definition-)
      "int8 supported_foot

---
bool success
")



(provide :movement_utils/balance "01c548ad4bcd6f9d88f95b8adc185129")


