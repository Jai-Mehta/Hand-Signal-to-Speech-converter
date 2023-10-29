import pyttsx3
def text_to_speech(mytext):
    engine = pyttsx3.init()
    engine.say(mytext)
    engine.runAndWait()
import numpy as np
def get_pcb(outs,width,height):
    preds=[]
    confi=[]
    boxes=[]
    for out in outs:
        for detection in out:
            scores = detection[5:]
            c_id = np.argmax(scores)
            confidence = scores[c_id]
            if confidence > 0.01:
                #onject detected
                center_x= int(detection[0]*width)
                center_y= int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x,y,w,h]) 
                confi.append(float(confidence))
                preds.append(c_id)
    return preds,confi,boxes