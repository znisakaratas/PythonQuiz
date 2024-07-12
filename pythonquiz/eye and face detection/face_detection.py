import cv2

face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap  = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize= (30,30), flags= cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x, y),(x+w, y+h),(0,255,0),2)

    cv2.imshow("video", frame)

    if cv2.waitKey(1)& 0xFF ==ord('4'):
        break


cap.release()
cv2.destroyAllWindows()