import os
import skeleton
import cv2

path='./Data/'

dirlist=[path+x for x in os.listdir(path)]

filelist=[]

for i in range(len(dirlist)):
	filelist.append([dirlist[i]+'/'+x for x in os.listdir(dirlist[i])])
hand = skeleton.hand()

"""
f0=open('test_points0.txt','w')
f1=open('test_points1.txt','w')
"""
for fdir in filelist:
	b=fdir[0].split('/')[2].split('_')[-1]
	text_file='output/train/'+fdir[0].split('/')[2]+'.txt'
	with open(text_file,'w') as f:
		for file in fdir:
			image =cv2.imread(file)
			catch_flag = hand.detection(image)

			f.write(str(hand.points)+'\n')



"""		
	for file in fdir:
		image =cv2.imread(file)
		catch_flag = hand.detection(image)

		if b=='true':
			f1.write(str(hand.points)+'\n')
		elif b=='false':
			f0.write(str(hand.points)+'\n')

f0.close()
f1.close()"""