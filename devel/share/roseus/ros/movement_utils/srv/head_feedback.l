;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::head_feedback)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'head_feedback (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::HEAD_FEEDBACK")
  (make-package "MOVEMENT_UTILS::HEAD_FEEDBACK"))
(unless (find-package "MOVEMENT_UTILS::HEAD_FEEDBACKREQUEST")
  (make-package "MOVEMENT_UTILS::HEAD_FEEDBACKREQUEST"))
(unless (find-package "MOVEMENT_UTILS::HEAD_FEEDBACKRESPONSE")
  (make-package "MOVEMENT_UTILS::HEAD_FEEDBACKRESPONSE"))

(in-package "ROS")





(defclass movement_utils::head_feedbackRequest
  :super ros::object
  :slots (_dont_use ))

(defmethod movement_utils::head_feedbackRequest
  (:init
   (&key
    ((:dont_use __dont_use) nil)
    )
   (send-super :init)
   (setq _dont_use __dont_use)
   self)
  (:dont_use
   (&optional (__dont_use :null))
   (if (not (eq __dont_use :null)) (setq _dont_use __dont_use)) _dont_use)
  (:serialization-length
   ()
   (+
    ;; bool _dont_use
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _dont_use
       (if _dont_use (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _dont_use
     (setq _dont_use (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass movement_utils::head_feedbackResponse
  :super ros::object
  :slots (_pos_vector ))

(defmethod movement_utils::head_feedbackResponse
  (:init
   (&key
    ((:pos_vector __pos_vector) (make-array 2 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _pos_vector __pos_vector)
   self)
  (:pos_vector
   (&optional __pos_vector)
   (if __pos_vector (setq _pos_vector __pos_vector)) _pos_vector)
  (:serialization-length
   ()
   (+
    ;; float32[2] _pos_vector
    (* 4    2)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[2] _pos_vector
     (dotimes (i 2)
       (sys::poke (elt _pos_vector i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[2] _pos_vector
   (dotimes (i (length _pos_vector))
     (setf (elt _pos_vector i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;;
   self)
  )

(defclass movement_utils::head_feedback
  :super ros::object
  :slots ())

(setf (get movement_utils::head_feedback :md5sum-) "a254b821d70340d5ccc8779b3f5e7d9c")
(setf (get movement_utils::head_feedback :datatype-) "movement_utils/head_feedback")
(setf (get movement_utils::head_feedback :request) movement_utils::head_feedbackRequest)
(setf (get movement_utils::head_feedback :response) movement_utils::head_feedbackResponse)

(defmethod movement_utils::head_feedbackRequest
  (:response () (instance movement_utils::head_feedbackResponse :init)))

(setf (get movement_utils::head_feedbackRequest :md5sum-) "a254b821d70340d5ccc8779b3f5e7d9c")
(setf (get movement_utils::head_feedbackRequest :datatype-) "movement_utils/head_feedbackRequest")
(setf (get movement_utils::head_feedbackRequest :definition-)
      "bool dont_use
---
float32[2] pos_vector
")

(setf (get movement_utils::head_feedbackResponse :md5sum-) "a254b821d70340d5ccc8779b3f5e7d9c")
(setf (get movement_utils::head_feedbackResponse :datatype-) "movement_utils/head_feedbackResponse")
(setf (get movement_utils::head_feedbackResponse :definition-)
      "bool dont_use
---
float32[2] pos_vector
")



(provide :movement_utils/head_feedback "a254b821d70340d5ccc8779b3f5e7d9c")


