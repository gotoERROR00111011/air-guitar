from model import Net
from detect import hand_detect
import torch

import cv2
import skeleton

import midi

if __name__ == "__main__":
    model=Net().to('cuda')     #모델 할당
    model.load_state_dict(torch.load('model/Net.pth'))  # 학습된 모델 로드
    
    hand = skeleton.hand()
    music = midi.midi()

    video_path = './media/hand_test.avi'    
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, image = cap.read()
        catch_flag = hand.detection(image)

        if not catch_flag:
            continue
        
        distanceX, distanceY = hand.get_distance()

        points=torch.FloatTensor(hand.points).view(1,-1).to('cuda')

        hand_state=hand_detect(model,points)

        hand_sign = hand_state
        melody = music.to_note(distanceX, distanceY)
        music.sound(hand_sign, melody)