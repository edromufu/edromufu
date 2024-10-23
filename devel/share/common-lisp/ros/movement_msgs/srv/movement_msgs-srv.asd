
(cl:in-package :asdf)

(defsystem "movement_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BehRequestSrv" :depends-on ("_package_BehRequestSrv"))
    (:file "_package_BehRequestSrv" :depends-on ("_package"))
    (:file "CommandToOpenCMSrv" :depends-on ("_package_CommandToOpenCMSrv"))
    (:file "_package_CommandToOpenCMSrv" :depends-on ("_package"))
    (:file "WalkTestParametersSrv" :depends-on ("_package_WalkTestParametersSrv"))
    (:file "_package_WalkTestParametersSrv" :depends-on ("_package"))
  ))