import cv2
import mediapipe as mp

# hat take detect kortey media pipe lagbe
hand_detector = mp.solutions.hands.Hands()
drawing_utlis = mp.solutions.drawing_utils
# video capture kora lagbe
cap = cv2.VideoCapture(0)
# video ta to choltei thakbe tai while loop use kora hoy
while True:
    _, frame = cap.read()
    # jehetu video ulta ashtese so flip kortey hbe
    frame= cv2.flip(frame,1)  # 1 mane y axis borabor ghurabe
    # kono ekta videio theke detect korle rgb moode e detect kora easy
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utlis.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for index,landmark in enumerate(landmarks):
                x = landmark.x
                y = landmark.y
                print(x,y)
    cv2.imshow('Virtual Mouse of Nakib',frame)
    cv2.waitKey(1)


