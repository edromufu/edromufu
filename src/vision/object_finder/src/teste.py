from ultralytics import YOLO
import cv2
import time

cap = cv2.VideoCapture(0,cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_BRIGHTNESS, (4))

# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
while True:
   
    ret , frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    #classes, scores, boxes, fps = ri.detect_model(self.model,frame)
    
    start_time = time.time()
    r=model.predict(source=frame,conf=0.25,show=True,device=0)
    classes, scores, boxes=r[0].boxes.cls,r[0].boxes.conf,r[0].boxes.xywh
    #r=model.predict(source=frame,conf=0.25,show=True,device='gpu',max_det=1)
    finish_time = time.time()
    fps = 1/(finish_time-start_time)

    print(r[0].boxes.xywh,'\n ==================')   #[xcenter,ycenter,wid-box,heigh-box]
                                #r[0] acessa os resultados
                                #r[0].boxes acessa os dados do box
    
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
    print(f"Classes: {classes}, Scores: {scores}")
    #print(f"Boxes: [x_center:{boxes[0]},y_center:{boxes[1]}, roi_width:{boxes[2]} roi_height:{boxes[3]}")
    #print(f"Boxes: {boxes}")
    #print('device: ', )
    print(f'FPS: {fps:.2f}')
    print('\n')

# Process results list
print('fim')