;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::page)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'page (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::PAGE")
  (make-package "MOVEMENT_UTILS::PAGE"))
(unless (find-package "MOVEMENT_UTILS::PAGEREQUEST")
  (make-package "MOVEMENT_UTILS::PAGEREQUEST"))
(unless (find-package "MOVEMENT_UTILS::PAGERESPONSE")
  (make-package "MOVEMENT_UTILS::PAGERESPONSE"))

(in-package "ROS")





(defclass movement_utils::pageRequest
  :super ros::object
  :slots (_page_name ))

(defmethod movement_utils::pageRequest
  (:init
   (&key
    ((:page_name __page_name) "")
    )
   (send-super :init)
   (setq _page_name (string __page_name))
   self)
  (:page_name
   (&optional __page_name)
   (if __page_name (setq _page_name __page_name)) _page_name)
  (:serialization-length
   ()
   (+
    ;; string _page_name
    4 (length _page_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _page_name
       (write-long (length _page_name) s) (princ _page_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _page_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _page_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass movement_utils::pageResponse
  :super ros::object
  :slots (_success ))

(defmethod movement_utils::pageResponse
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

(defclass movement_utils::page
  :super ros::object
  :slots ())

(setf (get movement_utils::page :md5sum-) "4f331e5d3a60dd4df8ef3fcaed28acb9")
(setf (get movement_utils::page :datatype-) "movement_utils/page")
(setf (get movement_utils::page :request) movement_utils::pageRequest)
(setf (get movement_utils::page :response) movement_utils::pageResponse)

(defmethod movement_utils::pageRequest
  (:response () (instance movement_utils::pageResponse :init)))

(setf (get movement_utils::pageRequest :md5sum-) "4f331e5d3a60dd4df8ef3fcaed28acb9")
(setf (get movement_utils::pageRequest :datatype-) "movement_utils/pageRequest")
(setf (get movement_utils::pageRequest :definition-)
      "string page_name
---
bool success
")

(setf (get movement_utils::pageResponse :md5sum-) "4f331e5d3a60dd4df8ef3fcaed28acb9")
(setf (get movement_utils::pageResponse :datatype-) "movement_utils/pageResponse")
(setf (get movement_utils::pageResponse :definition-)
      "string page_name
---
bool success
")



(provide :movement_utils/page "4f331e5d3a60dd4df8ef3fcaed28acb9")


