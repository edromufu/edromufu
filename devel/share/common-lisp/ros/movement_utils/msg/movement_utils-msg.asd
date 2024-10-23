
(cl:in-package :asdf)

(defsystem "movement_utils-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "body_motors_data" :depends-on ("_package_body_motors_data"))
    (:file "_package_body_motors_data" :depends-on ("_package"))
    (:file "head_motors_data" :depends-on ("_package_head_motors_data"))
    (:file "_package_head_motors_data" :depends-on ("_package"))
  ))