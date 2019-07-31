import cv2

def draw_area(image, rightX, rightY, distanceX):
	# sound area
	# -------------------------------
	# midi : 100 < distanceX < 300
	# this : area_sizeX = 200
	# -------------------------------
	# midi : 100 < distanceY < 400
	# this : area_sizeY = 300
	# -------------------------------

	area_sizeX = 200
	area_sizeY = 300

	# 오른손
	#cv2.rectangle(image, (rightX - 1, rightY - 1), (rightX + 1, rightY + 1), (255, 0, 0), 2)

	area_startX = rightX - int(area_sizeX / 2) + distanceX
	area_startY = rightY - int(area_sizeY / 2)
	area_endX = rightX + int(area_sizeX / 2) + distanceX
	area_endY = rightY + int(area_sizeY / 2)

	y = int((area_endY - area_startY) / 7)
	for row in range(1, 7):
		addY = y * row
		cv2.line(image, (area_startX, area_startY + addY), (area_endX, area_startY + addY), (0, 0, 255), 2)

	x = int((area_endX - area_startX) / 3)
	for col in range(1, 3):
		addX = x * col
		cv2.line(image, (area_startX + addX, area_startY), (area_startX + addX, area_endY), (0, 0, 255), 2)

	cv2.rectangle(image, (area_startX, area_startY), (area_endX, area_endY), (0, 0, 255), 2)

if __name__ == "__main__":

	cap = cv2.VideoCapture(0)

	while True:
		ret, image = cap.read()
		distanceX = 300
		rightX = 100
		rightY = 200

		draw_area(image, rightX, rightY, distanceX)

		cv2.imshow("Capture", image) 
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
