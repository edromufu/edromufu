;; Auto-generated. Do not edit!


(when (boundp 'modularized_bhv_msgs::moveRequest)
  (if (not (find-package "MODULARIZED_BHV_MSGS"))
    (make-package "MODULARIZED_BHV_MSGS"))
  (shadow 'moveRequest (find-package "MODULARIZED_BHV_MSGS")))
(unless (find-package "MODULARIZED_BHV_MSGS::MOVEREQUEST")
  (make-package "MODULARIZED_BHV_MSGS::MOVEREQUEST"))
(unless (find-package "MODULARIZED_BHV_MSGS::MOVEREQUESTREQUEST")
  (make-package "MODULARIZED_BHV_MSGS::MOVEREQUESTREQUEST"))
(unless (find-package "MODULARIZED_BHV_MSGS::MOVEREQUESTRESPONSE")
  (make-package "MODULARIZED_BHV_MSGS::MOVEREQUESTRESPONSE"))

(in-package "ROS")





(defclass modularized_bhv_msgs::moveRequestRequest
  :super ros::object
  :slots (_moveRequest ))

(defmethod modularized_bhv_msgs::moveRequestRequest
  (:init
   (&key
    ((:moveRequest __moveRequest) "")
    )
   (send-super :init)
   (setq _moveRequest (string __moveRequest))
   self)
  (:moveRequest
   (&optional __moveRequest)
   (if __moveRequest (setq _moveRequest __moveRequest)) _moveRequest)
  (:serialization-length
   ()
   (+
    ;; string _moveRequest
    4 (length _moveRequest)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _moveRequest
       (write-long (length _moveRequest) s) (princ _moveRequest s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _moveRequest
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _moveRequest (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass modularized_bhv_msgs::moveRequestResponse
  :super ros::object
  :slots (_success ))

(defmethod modularized_bhv_msgs::moveRequestResponse
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

(defclass modularized_bhv_msgs::moveRequest
  :super ros::object
  :slots ())

(setf (get modularized_bhv_msgs::moveRequest :md5sum-) "fa4c3676b8fc489dd65422b45b94f727")
(setf (get modularized_bhv_msgs::moveRequest :datatype-) "modularized_bhv_msgs/moveRequest")
(setf (get modularized_bhv_msgs::moveRequest :request) modularized_bhv_msgs::moveRequestRequest)
(setf (get modularized_bhv_msgs::moveRequest :response) modularized_bhv_msgs::moveRequestResponse)

(defmethod modularized_bhv_msgs::moveRequestRequest
  (:response () (instance modularized_bhv_msgs::moveRequestResponse :init)))

(setf (get modularized_bhv_msgs::moveRequestRequest :md5sum-) "fa4c3676b8fc489dd65422b45b94f727")
(setf (get modularized_bhv_msgs::moveRequestRequest :datatype-) "modularized_bhv_msgs/moveRequestRequest")
(setf (get modularized_bhv_msgs::moveRequestRequest :definition-)
      "string moveRequest
---
bool success

")

(setf (get modularized_bhv_msgs::moveRequestResponse :md5sum-) "fa4c3676b8fc489dd65422b45b94f727")
(setf (get modularized_bhv_msgs::moveRequestResponse :datatype-) "modularized_bhv_msgs/moveRequestResponse")
(setf (get modularized_bhv_msgs::moveRequestResponse :definition-)
      "string moveRequest
---
bool success

")



(provide :modularized_bhv_msgs/moveRequest "fa4c3676b8fc489dd65422b45b94f727")


