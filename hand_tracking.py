import cv2
import mediapipe as mp

class hand_detector:
    def __init__(self, mode=False, maxHands=2, detectionCon=1, trackCon=2):
        self.mode = mode
        self.maxHands = maxHands
        self.trackCon = trackCon
        self.detectionCon = detectionCon

        self.hands = mp.solutions.hands.Hands(self.maxHands, self.trackCon, self.detectionCon, self.mode)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:   
                if draw:  
                    self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
        return img

    def get_positions(self, img, handNo=0, draw=True):

        positions = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                        print(id, cx, cy)
                        positions.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return positions
