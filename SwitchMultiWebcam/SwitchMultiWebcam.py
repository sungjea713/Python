'''
v1.1
Switch multi USB webcam
Jay Kim

'''

import cv2
x = 0
cap = cv2.VideoCapture(x)
while True:
    if cv2.waitkey(10) & 0xFF == ord('t'):
        if x==0:
            x = 1
            cap = cv2.VideoCapture(1)
        elif x==1:
            x = 0
            cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
