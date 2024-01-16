from ultralytics import YOLO
import cv2
import time

cap = cv2.VideoCapture(0,cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_BRIGHTNESS, (4))

# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
while True:
    time2=time.time()
    ret , frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    time2f=time.time() 
    #classes, scores, boxes, fps = ri.detect_model(self.model,frame)
    
    start_time = time.time()
    
    r=model.predict(source=frame,conf=0.25,verbose=False,device=0,imgsz=(640,384),max_det=1)
    classes, scores, boxes=r[0].boxes.cls.tolist(),r[0].boxes.conf.tolist(),r[0].boxes.xywh.tolist()
    inference_frame=r[0].plot()

    
    cv2.imshow("Current Frame", inference_frame)   

    #boxes acessa os dados da detecção, cls.tolist() é a lista de classes detectadas, conf.tolist() é a lista de confiança das classes
    #r=model.predict(source=frame,conf=0.25,show=True,device='gpu',max_det=1)
    finish_time = time.time()
    fps = 1/(finish_time-start_time)
    
    #for obj in r[0].boxes:
    #    x_center=obj.xywh[0][0]
    #    y_center=obj.xywh[0][1]
    #    roi_width=obj.xywh[0][2]
    #    roi_height=obj.xywh[0][3]

    if cv2.waitKey(1) == 27 :
        cap.release()
        cv2.destroyAllWindows()
        break
    '''
    x_center=r[0].boxes.xywh[0][0]
    y_center=r[0].boxes.xywh[0][1]
    roi_width=r[0].boxes.xywh[0][2]
    roi_height=r[0].boxes.xywh[0][3]'''
    '''print(f"Classes: {classes}, Scores: {scores}")
    print(f"Boxes [x_center, y_center, roi_width, roi_height]: {boxes}")
    #print('device: ' )
    print(f'FPS: {fps:.2f}')
    print('\n')'''

    
    print(f"\n\nFPS: {(time2f-time2)}\nFPSri: {1/fps}\n\n")

# Process results list
print('fim')