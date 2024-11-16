;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::vx)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'vx (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::VX")
  (make-package "MOVEMENT_UTILS::VX"))
(unless (find-package "MOVEMENT_UTILS::VXREQUEST")
  (make-package "MOVEMENT_UTILS::VXREQUEST"))
(unless (find-package "MOVEMENT_UTILS::VXRESPONSE")
  (make-package "MOVEMENT_UTILS::VXRESPONSE"))

(in-package "ROS")





(defclass movement_utils::vxRequest
  :super ros::object
  :slots (_vx _distX ))

(defmethod movement_utils::vxRequest
  (:init
   (&key
    ((:vx __vx) 0.0)
    ((:distX __distX) 0.0)
    )
   (send-super :init)
   (setq _vx (float __vx))
   (setq _distX (float __distX))
   self)
  (:vx
   (&optional __vx)
   (if __vx (setq _vx __vx)) _vx)
  (:distX
   (&optional __distX)
   (if __distX (setq _distX __distX)) _distX)
  (:serialization-length
   ()
   (+
    ;; float32 _vx
    4
    ;; float32 _distX
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _vx
       (sys::poke _vx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _distX
       (sys::poke _distX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _vx
     (setq _vx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _distX
     (setq _distX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass movement_utils::vxResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::vxResponse
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

(defclass movement_utils::vx
  :super ros::object
  :slots ())

(setf (get movement_utils::vx :md5sum-) "fc98f3eaa33f7560afd31582a184e752")
(setf (get movement_utils::vx :datatype-) "movement_utils/vx")
(setf (get movement_utils::vx :request) movement_utils::vxRequest)
(setf (get movement_utils::vx :response) movement_utils::vxResponse)

(defmethod movement_utils::vxRequest
  (:response () (instance movement_utils::vxResponse :init)))

(setf (get movement_utils::vxRequest :md5sum-) "fc98f3eaa33f7560afd31582a184e752")
(setf (get movement_utils::vxRequest :datatype-) "movement_utils/vxRequest")
(setf (get movement_utils::vxRequest :definition-)
      "float32 vx
float32 distX
---
bool success
")

(setf (get movement_utils::vxResponse :md5sum-) "fc98f3eaa33f7560afd31582a184e752")
(setf (get movement_utils::vxResponse :datatype-) "movement_utils/vxResponse")
(setf (get movement_utils::vxResponse :definition-)
      "float32 vx
float32 distX
---
bool success
")



(provide :movement_utils/vx "fc98f3eaa33f7560afd31582a184e752")


