import cv2
import io
import time
import socket
import struct
import pickle

ip = 'win.cv-net.kro.kr'
username = ''
password = ''

IP = ip
PORT = 8485
img_counter = 0

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)
#cam.set(3, 320);
#cam.set(4, 240);

img_counter = 0
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)

    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

    time.sleep(0.2)
    #cv2.imshow('show', frame)
    #cv2.waitKey(100)

cam.release()
