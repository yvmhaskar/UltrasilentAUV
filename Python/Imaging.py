# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:41:37 2023

@author: mhask
"""

import cv2
from time import time


x=int(640)
y=int(480)

take_picture = True
pic_num = 1
time_last_pic = time()
end = time() + 240


#thres = 0.45 # Threshold to detect object

classNames = []
classFile = "/home/sealion2/Desktop/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/sealion2/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/sealion2/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)



def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    
    #if the banana is there print info
    global take_picture
    global pic_num
    
    num = 0
    
    if 'take_picture' in globals() and take_picture:
        result, image = cap.read()
        cv2.imwrite("/home/sealion2/Desktop/test.png",image)
        take_picture = False
    
    try:
        if classIds.any():
            #print(classIds,bbox)
            if pic_num < 10:
                result, image = cap.read()
                pic_num = pic_num + 1
    except:
        num = num + 1
        if num == 100:
            num = 0
        
        
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    print(box)
                    center=(int(x/2),int(y/2))
                    radius=2
                    xcoord=int((2*box[0]+box[2])/2)
                    ycoord=int((2*box[1]+box[3])/2)
                    center=(xcoord,ycoord)
                    yoff=(xcoord-x/2)
                    zoff=(-ycoord+y/2)
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.circle(img,center,radius,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return yoff,zoff

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #cap.set(10,70)


while time()<end:
    success, img = cap.read()
    result, objectInfo = getObjects(img,0.45,0.2,objects=['person'])
    #print(objectInfo)
    #cv2.imshow("Output",img)
    cv2.waitKey(1)
        
    if objectInfo and pic_num < 10 and take_picture:
        result, image = cap.read()
        #imshow("1",image)
        cv2.imwrite("/home/sealion2/Desktop/pict " + str(pic_num) + ".png",img)
        #save("1.png",image)
        print("Took picture #" + str(pic_num) + ".")
        pic_num = pic_num + 1
        take_picture = False
        time_last_pic = time()
    
    if time() - time_last_pic > 5:
        take_picture = True

    

print ('done')