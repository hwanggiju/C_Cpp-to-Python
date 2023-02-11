import cv2
import time

cap = cv2.VideoCapture(0)

if cap.isOpened() :
    delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))
    EndTime = 0
    while True :
        ret, img = cap.read()
        if ret :
            cv2.imshow("camera", img)
            
            if cv2.waitKey(delay) & 0xFF == 27 :
                print("ESC Pressed")
                break
        else :
            print(ret, img)
            break

else :
    print("camera not opened")
    
cap.release()
cv2.destroyAllWindows()