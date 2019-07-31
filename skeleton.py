import os
import sys
import cv2
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' +  dir_path + '/bin;'
import pyopenpose as op

class hand:
    def __init__(self):
        params = dict()
        params["model_folder"] = "./models/"
        #params["face"] = True
        params["hand"] = True

        self.leftX = []
        self.leftY = []
        self.left_centerX = 0
        self.left_centerY = 0
        self.right_centerX = 0 
        self.right_centerY = 0
        self.distanceX = 0
        self.distanceY = 0

        self.opWrapper = op.WrapperPython()
        self.opWrapper.configure(params)
        self.opWrapper.start()

    def detection(self, img):
        img = cv2.resize(img, (640, 360), fx=1.0, fy=1.0, interpolation=cv2.INTER_CUBIC)
        datum = op.Datum()
        datum.cvInputData = img
        self.opWrapper.emplaceAndPop([datum])

        #body = datum.poseKeypoints
        #face = datum.faceKeypoints
        left = datum.handKeypoints[0]
        right = datum.handKeypoints[1]

        if sum(left[0])[0] == 0. or sum(right[0])[0] == 0.:
            return False

        self.leftX = []
        self.leftY = []
        for l in left[0]:
            self.leftX.append(l[0])
            self.leftY.append(l[1])

        self.points=[]
        self.rightX = []
        self.rightY = []
        for r in right[0]:
            self.rightX.append(r[0])
            self.rightY.append(r[1])

            self.points.append(r[0])
            self.points.append(r[1])

        self.left_centerX, self.left_centerY = self.get_center(self.leftX, self.leftY)
        self.right_centerX, self.right_centerY = self.get_center(self.rightX, self.rightY)
        self.distanceX = abs(self.left_centerX - self.right_centerX)
        self.distanceY = abs(self.left_centerY - self.right_centerY)

        img = datum.cvOutputData
        self.draw_area(img)
        cv2.imshow("Pose and Hand", img)
        cv2.waitKey(1)
                
        return True

    def draw_area(self, image):
        # sound area
        # -------------------------------
        # midi : 100 < distanceX < 300
        # this : area_sizeX = 200 + distance(200)
        # -------------------------------
        # midi : -150 < distanceY < 150
        # this : area_sizeY = 300
        # -------------------------------
        distance = 200
        area_sizeX = 200
        area_sizeY = 300
        rightX = self.right_centerX
        rightY = self.right_centerY
        area_startX = int(rightX - (area_sizeX / 2)) + distance
        area_startY = int(rightY - (area_sizeY / 2))
        area_endX = int(rightX + (area_sizeX / 2)) + distance
        area_endY = int(rightY + (area_sizeY / 2))

        y = int((area_endY - area_startY) / 7)
        for row in range(1, 7):
            addY = y * row
            cv2.line(image, (area_startX, area_startY + addY), (area_endX, area_startY + addY), (0, 0, 255), 2)

        x = int((area_endX - area_startX) / 3)
        for col in range(1, 3):
            addX = x * col
            cv2.line(image, (area_startX + addX, area_startY), (area_startX + addX, area_endY), (0, 0, 255), 2)

        cv2.rectangle(image, (area_startX, area_startY), (area_endX, area_endY), (0, 0, 255), 2)

    def get_point(self):
        return self.leftX, self.leftY, self.rightX, self.rightY

    def get_center(self, X, Y):
        x = 0
        y = 0
        cnt = 0
        for i in range(len(X)):
            if X[i] == 0.: continue
            cnt += 1
            x += X[i]
            y += Y[i]
        x /= cnt
        y /= cnt

        return x, y

    def get_left_center(self):
        return self.left_centerX, self.left_centerY

    def get_right_center(self):
        return self.right_centerX, self.right_centerY

    def get_distance(self):
        return self.distanceX, self.distanceY
