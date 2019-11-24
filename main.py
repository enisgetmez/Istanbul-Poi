#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cascade
import mobese
import cv2
import imutils

cascadee = cascade.secili()
url = mobese.secili()

cap = cv2.VideoCapture(url)
haar_cascade = cv2.CascadeClassifier(cascadee)
while(True):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=1500 ,height=120) # görüntü genişliğini 600p yapıyoruz
    frame = imutils.rotate(frame, angle=0) # görüntüyü sabitliyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #griye çeviriyoruz
    #yuzleri tespit ediyoruz
    casc = haar_cascade.detectMultiScale(gray, 1.3, 2)
    #tespit edilen yuzlerin etrafini ciziyoruz 
    for (x,y,w,h) in casc:
        cv2.rectangle(frame,(x+5,y+5),(x+w-5,y+h-5),(0,255,0),2)   
    #ekranda gosteriyoruz
    cv2.putText(frame, "Anlik olarak tespit: " + str(len(casc)), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 1,  (255,255,255), 1)
    cv2.imshow('Detect', frame)
    #q tusu cikis
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()