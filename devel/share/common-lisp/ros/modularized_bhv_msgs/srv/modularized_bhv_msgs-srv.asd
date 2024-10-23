
(cl:in-package :asdf)

(defsystem "modularized_bhv_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "moveRequest" :depends-on ("_package_moveRequest"))
    (:file "_package_moveRequest" :depends-on ("_package"))
  ))