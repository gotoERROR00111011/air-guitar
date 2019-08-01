import cv2
import socket
import sys
import pickle
import numpy as np
import struct
import torch

import midi
import skeleton
from model import Net
from detect import hand_detect

if __name__ == '__main__':
    model=Net().to('cuda')
    model.load_state_dict(torch.load('model/Net.pth'))
    
    hand = skeleton.hand()
    music = midi.midi()

    HOST = 'win.cv-net.kro.kr'
    PORT = 8485

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')

    conn, addr = s.accept()

    data = b""
    payload_size = struct.calcsize(">L")
    print("payload_size: {}".format(payload_size))

    while True:
        while len(data) < payload_size:
            #print("Recv: {}".format(len(data)))
            data += conn.recv(4096)

        #print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        #print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        if not hand.detection(frame):
            continue
        distanceX, distanceY = hand.get_distance()

        points = torch.FloatTensor(hand.points).view(1, -1).to('cuda')
        hand_sign = hand_detect(model, points)

        melody = music.to_note(distanceX, distanceY)
        music.sound(hand_sign, melody)        

    #hand.out.release()
