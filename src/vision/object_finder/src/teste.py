from ultralytics import YOLO
import cv2
import time

cap = cv2.VideoCapture(0,cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_BRIGHTNESS, (4))

# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
while True:
   
    ret , frame = cap.read()
    #frame = cv2.resize(frame, (640,480))
    #classes, scores, boxes, fps = ri.detect_model(self.model,frame)
    
    start_time = time.time()
    #results = model(frame)
    r=model.predict(source=frame,conf=0.25,show=True)
    #r=model.predict(source=frame,conf=0.25,show=True,device='gpu',max_det=1)
    finish_time = time.time()
    fps = 1/(finish_time-start_time)

    print(r[0].boxes)

    print(r[0].boxes.xywh[0],'\n ==================')   #[xcenter,ycenter,wid-box,heigh-box]
                                #r[0] acessa os resultados
                                #r[0].boxes acessa os dados do box
    
    for obj in r[0].boxes:
        #print(item)
        x_center=obj.xywh[0][0]
        y_center=obj.xywh[0][1]
        roi_width=obj.xywh[0][2]
        roi_height=obj.xywh[0][3]

    if cv2.waitKey(1) == ord("q") :
        cap.release()
        cv2.destroyAllWindows()
        break

    '''i=list(r[0].boxes.cls).index(0)
    x_center=r[0].boxes[i].xywh[0][0]
    y_center=r[0].boxes[i].xywh[0][1]
    roi_width=r[0].boxes[i].xywh[0][2]
    roi_height=r[0].boxes[i].xywh[0][3]
    print(f"Classes: {r[0].boxes.cls[0]}, Scores: {r[0].boxes.conf[0]}")
    print(f"Boxes: {x_center},{y_center}, {roi_width} {roi_height}")'''
    print(f'FPS: {fps:.2f}')
    print('\n')

# Process results list
print('fim')