import os
import sys
import cv2
import math

def hand_detection(img):
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(dir_path + '/python/openpose/Release');
    os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' +  dir_path + '/bin;'
    import pyopenpose as op

    params = dict()
    params["model_folder"] = "./models/"
    #params["face"] = True
    params["hand"] = True

    try:
        opWrapper = op.WrapperPython()
        opWrapper.configure(params)
        opWrapper.start()

        datum = op.Datum()
        #imageToProcess = cv2.imread(img_path)
        imageToProcess = img
        datum.cvInputData = imageToProcess

        opWrapper.emplaceAndPop([datum])

        #body = str(datum.poseKeypoints)
        #face = str(datum.faceKeypoints)
        left = datum.handKeypoints[0]
        right = datum.handKeypoints[1]

        leftX = []
        leftY = []
        for l in left[0]:
            leftX.append(l[0])
            leftY.append(l[1])
        rightX = []
        rightY = []
        for r in right[0]:
            rightX.append(r[0])
            rightY.append(r[1])

        #cv2.imshow("Pose and Hand", datum.cvOutputData)
        #cv2.waitKey(0)

    except Exception as e:
        sys.exit(-1)

    print('TEST')

    return leftX, leftY, rightX, rightY


def hand_center(X, Y):
    cnt = 0
    x = 0
    y = 0

    for i in range(len(X)):
        if X[i] == 0.: continue
        cnt += 1
        x += X[i]
        y += Y[i]

    x /= cnt
    y /= cnt

    return x, y

def hand_distance(leftX, leftY, rightX, rightY):
    x = abs(leftX - rightX)
    y = abs(leftY - rightY)
    return x, y


img = cv2.imread('./test/img.jpg')

leftX, leftY, rightX, rightY = hand_detection(img)
print(leftX)
print(leftY)
print(rightX)
print(rightY)
