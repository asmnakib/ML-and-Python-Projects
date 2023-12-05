import cv2
# video capture kora lagbe
cap = cv2.VideoCapture(0)
# video ta to choltei thakbe tai while loop use kora hoy
while True:
    _, frame = cap.read()
    cv2.imshow('Virtual Mouse of Nakib',frame)
    cv2.waitKey(1)


