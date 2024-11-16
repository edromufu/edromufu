;; Auto-generated. Do not edit!


(when (boundp 'movement_utils::body_motors_data)
  (if (not (find-package "MOVEMENT_UTILS"))
    (make-package "MOVEMENT_UTILS"))
  (shadow 'body_motors_data (find-package "MOVEMENT_UTILS")))
(unless (find-package "MOVEMENT_UTILS::BODY_MOTORS_DATA")
  (make-package "MOVEMENT_UTILS::BODY_MOTORS_DATA"))

(in-package "ROS")
;;//! \htmlinclude body_motors_data.msg.html


(defclass movement_utils::body_motors_data
  :super ros::object
  :slots (_pos_vector ))

(defmethod movement_utils::body_motors_data
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

(setf (get movement_utils::body_motors_data :md5sum-) "18af1fa9d2e7d06f4ff52d42169a41bd")
(setf (get movement_utils::body_motors_data :datatype-) "movement_utils/body_motors_data")
(setf (get movement_utils::body_motors_data :definition-)
      "float32[18] pos_vector
")



(provide :movement_utils/body_motors_data "18af1fa9d2e7d06f4ff52d42169a41bd")


