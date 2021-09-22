import cv2

cap = cv2.VideoCapture(0)
Cascade_Classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,0)
    detections = Cascade_Classifier.detectMultiScale(gray, 1.1, 5)


    if(len(detections)>0):
        (x,y,w,h)= detections[0]
        frame= cv2.rectangle(frame,(x,y)(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyWindow()


