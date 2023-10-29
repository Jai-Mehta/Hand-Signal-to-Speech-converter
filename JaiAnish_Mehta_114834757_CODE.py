import cv2
import numpy as np
import time
from modules import text_to_speech,get_pcb
weights = cv2.dnn.readNet("./Additional/training.weights", "./Additional/testing.cfg")
classes = []
with open("./Additional/unique_classes.txt","r") as f:
    classes = [line.strip() for line in f.readlines()]
layers = weights.getLayerNames()
outputlayers = []
for i in weights.getUnconnectedOutLayers():
    outputlayers.append(layers[i - 1])
colors= np.random.uniform(0,255,size=(len(classes),3))
cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

font = cv2.FONT_HERSHEY_PLAIN
starting_time= time.time()
frame_id = 0
while True:
    _,frame= cap.read()
    frame_id+=1
    height,width,channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame,0.00392,(320,320),(0,0,0),True,crop=False)
    weights.setInput(blob)
    outs = weights.forward(outputlayers)
    preds,confi,boxes = get_pcb(outs,width,height)
    predicted_classes = cv2.dnn.NMSBoxes(boxes,confi,0.4,0.6)
    for i in range(len(boxes)):
        if i in predicted_classes:
            x,y,w,h = boxes[i]
            label = str(classes[preds[i]])
            print(label)
            if label =="Cancel":
                cap.release()    
                cv2.destroyAllWindows()
            else:
                text_to_speech(label)
            confidence= confi[i]
            color = colors[preds[i]]
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
            cv2.putText(frame,label+" "+str(round(confidence,2)),(x,y+30),font,1,(255,255,255),2)
    elapsed_time = time.time() - starting_time
    fps=frame_id/elapsed_time
    cv2.putText(frame,"FPS:"+str(round(fps,2)),(10,50),font,2,(0,0,0),1)
    cv2.imshow("Image",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()    
cv2.destroyAllWindows()