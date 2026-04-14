import cv2

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("The camera can't open")
else:
    print("Camera is open")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("cannot read the camera frame")
        break

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Q for quit
        break

cap.release()
cv2.destroyAllWindows()
