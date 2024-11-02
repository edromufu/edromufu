;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::body_feedback)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'body_feedback (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::BODY_FEEDBACK")
  (make-package "MOVEMENT_UTILS::BODY_FEEDBACK"))
(unless (find-package "MOVEMENT_UTILS::BODY_FEEDBACKREQUEST")
  (make-package "MOVEMENT_UTILS::BODY_FEEDBACKREQUEST"))
(unless (find-package "MOVEMENT_UTILS::BODY_FEEDBACKRESPONSE")
  (make-package "MOVEMENT_UTILS::BODY_FEEDBACKRESPONSE"))

(in-package "ROS")





(defclass movement_utils::body_feedbackRequest
  :super ros::object
  :slots (_dont_use ))

(defmethod movement_utils::body_feedbackRequest
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

(defclass movement_utils::body_feedbackResponse
  :super ros::object
  :slots (_pos_vector ))

(defmethod movement_utils::body_feedbackResponse
  (:init
   (&key
    ((:pos_vector __pos_vector) (make-array 18 :initial-element 0.0 :element-type :float))
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
    ;; float32[18] _pos_vector
    (* 4    18)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[18] _pos_vector
     (dotimes (i 18)
       (sys::poke (elt _pos_vector i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[18] _pos_vector
   (dotimes (i (length _pos_vector))
     (setf (elt _pos_vector i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;;
   self)
  )

(defclass movement_utils::body_feedback
  :super ros::object
  :slots ())

(setf (get movement_utils::body_feedback :md5sum-) "1e559a2e011119a9aa759d0e8a946d1f")
(setf (get movement_utils::body_feedback :datatype-) "movement_utils/body_feedback")
(setf (get movement_utils::body_feedback :request) movement_utils::body_feedbackRequest)
(setf (get movement_utils::body_feedback :response) movement_utils::body_feedbackResponse)

(defmethod movement_utils::body_feedbackRequest
  (:response () (instance movement_utils::body_feedbackResponse :init)))

(setf (get movement_utils::body_feedbackRequest :md5sum-) "1e559a2e011119a9aa759d0e8a946d1f")
(setf (get movement_utils::body_feedbackRequest :datatype-) "movement_utils/body_feedbackRequest")
(setf (get movement_utils::body_feedbackRequest :definition-)
      "bool dont_use
---
float32[18] pos_vector
")

(setf (get movement_utils::body_feedbackResponse :md5sum-) "1e559a2e011119a9aa759d0e8a946d1f")
(setf (get movement_utils::body_feedbackResponse :datatype-) "movement_utils/body_feedbackResponse")
(setf (get movement_utils::body_feedbackResponse :definition-)
      "bool dont_use
---
float32[18] pos_vector
")



(provide :movement_utils/body_feedback "1e559a2e011119a9aa759d0e8a946d1f")


