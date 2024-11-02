;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::enable_torque)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'enable_torque (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::ENABLE_TORQUE")
  (make-package "MOVEMENT_UTILS::ENABLE_TORQUE"))
(unless (find-package "MOVEMENT_UTILS::ENABLE_TORQUEREQUEST")
  (make-package "MOVEMENT_UTILS::ENABLE_TORQUEREQUEST"))
(unless (find-package "MOVEMENT_UTILS::ENABLE_TORQUERESPONSE")
  (make-package "MOVEMENT_UTILS::ENABLE_TORQUERESPONSE"))

(in-package "ROS")





(defclass movement_utils::enable_torqueRequest
  :super ros::object
  :slots (_data _motor_ids ))

(defmethod movement_utils::enable_torqueRequest
  (:init
   (&key
    ((:data __data) nil)
    ((:motor_ids __motor_ids) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _data __data)
   (setq _motor_ids __motor_ids)
   self)
  (:data
   (&optional (__data :null))
   (if (not (eq __data :null)) (setq _data __data)) _data)
  (:motor_ids
   (&optional __motor_ids)
   (if __motor_ids (setq _motor_ids __motor_ids)) _motor_ids)
  (:serialization-length
   ()
   (+
    ;; bool _data
    1
    ;; int8[] _motor_ids
    (* 1    (length _motor_ids)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _data
       (if _data (write-byte -1 s) (write-byte 0 s))
     ;; int8[] _motor_ids
     (write-long (length _motor_ids) s)
     (dotimes (i (length _motor_ids))
       (write-byte (elt _motor_ids i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _data
     (setq _data (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8[] _motor_ids
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _motor_ids (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _motor_ids i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _motor_ids i) 127) (setf (elt _motor_ids i) (- (elt _motor_ids i) 256)))
     ))
   ;;
   self)
  )

(defclass movement_utils::enable_torqueResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::enable_torqueResponse
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

(defclass movement_utils::enable_torque
  :super ros::object
  :slots ())

(setf (get movement_utils::enable_torque :md5sum-) "56c16441f9caa9412e348ec2e61432df")
(setf (get movement_utils::enable_torque :datatype-) "movement_utils/enable_torque")
(setf (get movement_utils::enable_torque :request) movement_utils::enable_torqueRequest)
(setf (get movement_utils::enable_torque :response) movement_utils::enable_torqueResponse)

(defmethod movement_utils::enable_torqueRequest
  (:response () (instance movement_utils::enable_torqueResponse :init)))

(setf (get movement_utils::enable_torqueRequest :md5sum-) "56c16441f9caa9412e348ec2e61432df")
(setf (get movement_utils::enable_torqueRequest :datatype-) "movement_utils/enable_torqueRequest")
(setf (get movement_utils::enable_torqueRequest :definition-)
      "bool data
int8[] motor_ids
---
bool success
")

(setf (get movement_utils::enable_torqueResponse :md5sum-) "56c16441f9caa9412e348ec2e61432df")
(setf (get movement_utils::enable_torqueResponse :datatype-) "movement_utils/enable_torqueResponse")
(setf (get movement_utils::enable_torqueResponse :definition-)
      "bool data
int8[] motor_ids
---
bool success
")



(provide :movement_utils/enable_torque "56c16441f9caa9412e348ec2e61432df")


