import modules.hand_tracking 
import modules.video
from pipeop import pipes

video_player = modules.video.video_player()
fps_counter = modules.video.fps_counter()

hand_detector = modules.hand_tracking.hand_detector()


@pipes
def detect_hands():
        while True:
                hands_video = video_player.get_frames() >> hand_detector.find_hands()
                
                positions = hands_video >> hand_detector.get_positions()
                
                if len(positions) > 0: print(positions[4])
                
                hands_video >> video_player.show_video(fps_counter.get_fps()) 

detect_hands()
