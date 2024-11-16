
(cl:in-package :asdf)

(defsystem "vision_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "Ball" :depends-on ("_package_Ball"))
    (:file "_package_Ball" :depends-on ("_package"))
    (:file "Goal" :depends-on ("_package_Goal"))
    (:file "_package_Goal" :depends-on ("_package"))
    (:file "Leftgoalpost" :depends-on ("_package_Leftgoalpost"))
    (:file "_package_Leftgoalpost" :depends-on ("_package"))
    (:file "Objects" :depends-on ("_package_Objects"))
    (:file "_package_Objects" :depends-on ("_package"))
    (:file "Rightgoalpost" :depends-on ("_package_Rightgoalpost"))
    (:file "_package_Rightgoalpost" :depends-on ("_package"))
    (:file "Robot" :depends-on ("_package_Robot"))
    (:file "_package_Robot" :depends-on ("_package"))
    (:file "Webotsmsg" :depends-on ("_package_Webotsmsg"))
    (:file "_package_Webotsmsg" :depends-on ("_package"))
  ))