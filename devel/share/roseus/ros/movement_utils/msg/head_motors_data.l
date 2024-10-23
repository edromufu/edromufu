;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::head_motors_data)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'head_motors_data (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::HEAD_MOTORS_DATA")
  (make-package "MOVEMENT_UTILS::HEAD_MOTORS_DATA"))

(in-package "ROS")
;;//! \htmlinclude head_motors_data.msg.html


(defclass movement_utils::head_motors_data
  :super ros::object
  :slots (_pos_vector ))

(defmethod movement_utils::head_motors_data
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

(setf (get movement_utils::head_motors_data :md5sum-) "019f44c03fbd0840875f997c96bee773")
(setf (get movement_utils::head_motors_data :datatype-) "movement_utils/head_motors_data")
(setf (get movement_utils::head_motors_data :definition-)
      "float32[2] pos_vector
")



(provide :movement_utils/head_motors_data "019f44c03fbd0840875f997c96bee773")


