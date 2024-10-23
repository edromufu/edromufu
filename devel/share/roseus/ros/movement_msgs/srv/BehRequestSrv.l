;; Auto-generated. Do not edit!


(when (boundp 'movement_msgs::BehRequestSrv)
  (if (not (find-package "MOVEMENT_MSGS"))
    (make-package "MOVEMENT_MSGS"))
  (shadow 'BehRequestSrv (find-package "MOVEMENT_MSGS")))
(unless (find-package "MOVEMENT_MSGS::BEHREQUESTSRV")
  (make-package "MOVEMENT_MSGS::BEHREQUESTSRV"))
(unless (find-package "MOVEMENT_MSGS::BEHREQUESTSRVREQUEST")
  (make-package "MOVEMENT_MSGS::BEHREQUESTSRVREQUEST"))
(unless (find-package "MOVEMENT_MSGS::BEHREQUESTSRVRESPONSE")
  (make-package "MOVEMENT_MSGS::BEHREQUESTSRVRESPONSE"))

(in-package "ROS")





(defclass movement_msgs::BehRequestSrvRequest
  :super ros::object
  :slots (_required_movement _required_status ))

(defmethod movement_msgs::BehRequestSrvRequest
  (:init
   (&key
    ((:required_movement __required_movement) "")
    ((:required_status __required_status) nil)
    )
   (send-super :init)
   (setq _required_movement (string __required_movement))
   (setq _required_status __required_status)
   self)
  (:required_movement
   (&optional __required_movement)
   (if __required_movement (setq _required_movement __required_movement)) _required_movement)
  (:required_status
   (&optional (__required_status :null))
   (if (not (eq __required_status :null)) (setq _required_status __required_status)) _required_status)
  (:serialization-length
   ()
   (+
    ;; string _required_movement
    4 (length _required_movement)
    ;; bool _required_status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _required_movement
       (write-long (length _required_movement) s) (princ _required_movement s)
     ;; bool _required_status
       (if _required_status (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _required_movement
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _required_movement (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _required_status
     (setq _required_status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass movement_msgs::BehRequestSrvResponse
  :super ros::object
  :slots (_response ))

(defmethod movement_msgs::BehRequestSrvResponse
  (:init
   (&key
    ((:response __response) nil)
    )
   (send-super :init)
   (setq _response __response)
   self)
  (:response
   (&optional (__response :null))
   (if (not (eq __response :null)) (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; bool _response
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _response
       (if _response (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _response
     (setq _response (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass movement_msgs::BehRequestSrv
  :super ros::object
  :slots ())

(setf (get movement_msgs::BehRequestSrv :md5sum-) "4f5d36d25e04a31db12adbc950d9b1a5")
(setf (get movement_msgs::BehRequestSrv :datatype-) "movement_msgs/BehRequestSrv")
(setf (get movement_msgs::BehRequestSrv :request) movement_msgs::BehRequestSrvRequest)
(setf (get movement_msgs::BehRequestSrv :response) movement_msgs::BehRequestSrvResponse)

(defmethod movement_msgs::BehRequestSrvRequest
  (:response () (instance movement_msgs::BehRequestSrvResponse :init)))

(setf (get movement_msgs::BehRequestSrvRequest :md5sum-) "4f5d36d25e04a31db12adbc950d9b1a5")
(setf (get movement_msgs::BehRequestSrvRequest :datatype-) "movement_msgs/BehRequestSrvRequest")
(setf (get movement_msgs::BehRequestSrvRequest :definition-)
      "string required_movement
bool required_status
---

bool response

")

(setf (get movement_msgs::BehRequestSrvResponse :md5sum-) "4f5d36d25e04a31db12adbc950d9b1a5")
(setf (get movement_msgs::BehRequestSrvResponse :datatype-) "movement_msgs/BehRequestSrvResponse")
(setf (get movement_msgs::BehRequestSrvResponse :definition-)
      "string required_movement
bool required_status
---

bool response

")



(provide :movement_msgs/BehRequestSrv "4f5d36d25e04a31db12adbc950d9b1a5")


