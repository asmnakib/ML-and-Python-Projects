import cv2
import mediapipe as mp
import pyautogui

# hat take detect kortey media pipe lagbe
hand_detector = mp.solutions.hands.Hands()
drawing_utlis = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size( )
# video capture kora lagbe
cap = cv2.VideoCapture(0)
# video ta to choltei thakbe tai while loop use kora hoy
while True:
    _, frame = cap.read()
    # jehetu video ulta ashtese so flip kortey hbe
    frame = cv2.flip(frame,1)  # 1 mane y axis borabor ghurabe
    # kono ekta videio theke detect korle rgb moode e detect kora easy
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # frame er height and wir=dth ber kora kora, kno? karon amd=r hand data gula k decimal point e rakhse amdr data gula k decimal kora lagbe
    frame_height, frame_width,_ = frame.shape
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utlis.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                # x axis er percentage er shthe frame er height diye gun kore dibo # fraction ashe output so int kore nibo
                x = int(landmark.x * frame_width)
                # y axis er percentages er shathe frame er width diye dibo
                y = int(landmark.y * frame_height)
                if id == 8:
                    # drawing circle
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / frame_width *x
                    index_y = screen_height /frame_height *y
                    pyautogui.moveTo(index_x,index_y)
    cv2.imshow('Virtual Mouse of Nakib',frame)
    cv2.waitKey(1)


