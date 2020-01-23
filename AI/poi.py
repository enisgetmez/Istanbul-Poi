import numpy as np
import cv2
import mobese
import datetime
from openpyxl import Workbook
kitap = Workbook() 
kitap.create_sheet("veriler") 
yaz = kitap.get_sheet_by_name("veriler") 
yaz.append(['Label','Count','Xcoordinate','Ycoordinate','Date-Time']) 


url = mobese.secili()
confidenceThreshold = 0.5
NMSThreshold = 0.3
modelConfiguration = 'yolov3.cfg'
modelWeights = 'yolov3.weights'
labelsPath = 'coco.names'
labels = open(labelsPath).read().strip().split('\n')
np.random.seed(10)
COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
outputLayer = net.getLayerNames()
outputLayer = [outputLayer[i[0] - 1] for i in net.getUnconnectedOutLayers()]
video_capture = cv2.VideoCapture(url)
(W, H) = (None, None)


while True:

    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    hebele = 0
    car = 0
    motorbike = 0
    handbag = 0
    if W is None or H is None:
        (H,W) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB = True, crop = False)
    net.setInput(blob)
    layersOutputs = net.forward(outputLayer)

    boxes = []
    confidences = []
    classIDs = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidenceThreshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY,  width, height) = box.astype('int')
                x = int(centerX - (width/2))
                y = int(centerY - (height/2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    detectionNMS = cv2.dnn.NMSBoxes(boxes, confidences, confidenceThreshold, NMSThreshold)
    if(len(detectionNMS) > 0):
        for i in detectionNMS.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            if(labels[classIDs[i]] == "person" ):
            	hebele+=1
            	yaz.append(['person',hebele,x,y,datetime.datetime.now()]) 
            	print(x,y)
            	print("Tespit Edilen İnsan Sayısı Anlık : " , str(hebele))
            	kitap.save("veriler.xlsx") # exceli kaydet
            if(labels[classIDs[i]] == "car" ):
            	car+=1
            	yaz.append(['car',car,x,y,datetime.datetime.now()]) 
            	print(x,y)
            	print("Tespit Edilen Araba Sayısı Anlık : " , str(hebele))
            	kitap.save("veriler.xlsx") # exceli kaydet
            if(labels[classIDs[i]] == "motorbike" ):
            	motorbike+=1
            	yaz.append(['motorbike',car,x,y,datetime.datetime.now()]) 
            	print(x,y)
            	print("Tespit Edilen motor Sayısı Anlık : " , str(hebele))
            	kitap.save("veriler.xlsx") # exceli kaydet


            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = '{}: {:.4f}'.format(labels[classIDs[i]], confidences[i])
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)



    cv2.imshow('sonuc', frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
    	break

kitap.close() #excelli kapat
video_capture.release()
cv2.destroyAllWindows()
