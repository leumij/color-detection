# https://www.youtube.com/watch?v=Tj4zEX_pdUg&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=10

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()