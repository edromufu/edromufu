from logging import exception
import cv2
import numpy as np

# cont = 1

# while cont < 6:

#     try:
#         print("Video" + str(cont))
#         webcam = cv2.VideoCapture("/dev/video" + str(cont))

#         while True:
#             conectado, frame = webcam.read()

#             cv2.imshow('Video original', frame)

#             key = cv2.waitKey(5)

#             if key == 27:      #tecla ESC fecha as janelas
#                 break

#     except Exception:
#         cont += 1

webcam = cv2.VideoCapture("/dev/video2")

while True:
    conectado, frame = webcam.read()
    frame = cv2.resize(frame, (640,480))

    cv2.imshow('Video original', frame)

    key = cv2.waitKey(5)

    if key == 27:      #tecla ESC fecha as janelas
        break

webcam.release()
cv2.destroyAllWindows()