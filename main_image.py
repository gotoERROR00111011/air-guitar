from model import Net
from detect import hand_detect
import torch

import cv2
import skeleton
import os
import midi

if __name__ == "__main__":
    model=Net().to('cuda')     #모델 할당
    model.load_state_dict(torch.load('model/Net.pth'))  # 학습된 모델 로드
    
    hand = skeleton.hand()
    music = midi.midi()

    path='./test/true/'

    output0=0
    output1=0

    image_list=[path+x for x in os.listdir(path)]
    for image_path in image_list:
        image =cv2.imread(image_path)

        catch_flag = hand.detection(image)

        leftX, leftY = hand.get_left_center()
        rightX, rightY = hand.get_right_center()
        distanceX, distanceY = hand.get_distance()

        points=torch.FloatTensor(hand.points).view(1,-1).to('cuda')

        hand_state=hand_detect(model,points)

        hand_sign = hand_state
        melody = music.to_note(distanceX, distanceY)
        if melody == -1:
            continue
        music.sound(hand_sign, melody)

        print(distanceX,distanceY)
        print('melody =',melody)