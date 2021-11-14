import cv2
import time

class video_player:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame_idx = 0
    def get_frames(self):
        success, frames = self.video_capture.read()
        return frames
    def show_video(self, image, fps):
        cv2.putText(image, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow("Image", image)
        cv2.waitKey(1)

class fps_counter:
    def __init__(self):
        self.start = 0
        self.end = time.time()
        self.fps = 0
    def update(self):
        self.end = time.time()
        self.fps = 1/(self.end-self.start)
        self.start = time.time()
    def get_fps(self):
        self.update()
        return str(int(self.fps))
