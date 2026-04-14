import cv2
# for part of cv2.CascadeClassifier place the model location with model name if u need a simple plan, just press ctrl + shift + c and then just paste (ctrl+v) to the models variable
# for frontalface model u can download by following this link: https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# for eye model u can download by following this link:: https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

face_cascade = cv2.CascadeClassifier(r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\haarcascade_frontalface_default.xml') # face model
eyeDetector = cv2.CascadeClassifier(r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\haarcascade_eye.xml') # eyes model

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2) # B,G,R: Blue, Green, Red (0,255,0) in 0 - 255 range
        roiAbuabu = gray[y:y+h,x:x+w]
        roiWarna = frame[y:y+h,x:x+w]
        mata = eyeDetector.detectMultiScale(roiAbuabu)
        for (xe,ye,we,he) in mata :
            cv2.rectangle(roiWarna,(xe,ye),(xe+we,ye+he),(0,0,255),1)
        
    cv2.imshow('Testing', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
