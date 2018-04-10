import pprint as pp
import time
import numpy as np
from random import randint
import math
# def chunks(l, n): 
	# for i in range(0, len(l), n):
		# return l[i:i + n]

		
def slidingWindow(image, windowSize):
	tmp = []
	# image = np.array(image)
	# pp.pprint(image)
	print('window sizw ', windowSize)
	print('Amount of rows', len(image))
	print()
	# pp.pprint(image)
	width = len(image)
	height = len(image[0])
	# Segments image into window sized chunks along the x axis
	for y in range(0, width, windowSize):
		for x in range(0, height, windowSize):
			# print("x : {} y : {} ".format(x, y))
			maximum = 0
			for innerX in range(x, x + windowSize):
				for innerY in range(y, y + windowSize):
					# print(image[innerY][innerX])
					if innerX >= height or innerY >= len(image):
						break
					else:
						# print("x : {} y : {} \nval : {}\n=========".format(innerX, innerY, image[innerY][innerX]))
						maximum = max(maximum, image[innerY][innerX])
			for innerX in range(x, x + windowSize):
				for innerY in range(y, y + windowSize):
					# print(image[innerY][innerX])
					if innerX >= height or innerY >= width:
						break
					else:
						# print("x : {} y : {} \nval : {}\n=========".format(innerX, innerY, image[innerY][innerX]))
						image[innerY][innerX] = maximum
			# print('max : {}'.format(maximum))
			# print("change place \n\n")
			
			# pp.pprint(image[y:y + windowSize, x:x + windowSize])
			# pp.pprint(max(image[y:y + windowSize, x:x + windowSize]))
			# tmp.append(sum(image[y:y + windowSize, x:x + windowSize]))
		# image[idx] = tmp
	# tmp = []
	# pp.pprint(tmp)
	size = len(image)
	# pp.pprint(image)
	fin = []
	# pp.pprint(image)
	
	# for idx, row in enumerate(image):
		# tmp.append(row)
		# if (idx + 1) % windowSize == 0:
			# fin.append(sum(x) for x in zip(*tmp))
			# tmp = []
	# fin.append(sum(x) for x in zip(*tmp))
	# for x in fin:
		# for y in x:
			# print(y)
	# merges chunks along the y axis 
	# for x in range(0, len(image), windowSize):
		# tmp.append(image[row])
		# fin.append(zip(*image[x:x + windowSize]))
		# print(image[x:x + windowSize])

	# for x in fin:
		# for y in x :
			# print("dsf")		
			# pp.pprint(y)
	# pp.pprint(zip(*image))

def slide(im, window, width, height):

	# Number of chunks which are produced
	max = [None] * math.ceil(math.ceil(width / window) * math.ceil(height / window))
	# print(len(max))
	innerMax = 0
	count = 0
	mov = 0
	rows = 0
	imSize = len(im)
	# t1 = time.time()
	for idx in range(0, imSize):
		pos = idx % width
		if im[idx] > innerMax:
			# If current value is new max replace old max
			innerMax = im[idx]
		if (pos + 1) % width == 0:
			# if the next value is on a new row
			# Set max 
			max[count] = innerMax
			innerMax = 0
			# set index in max array back to the start
			count = mov
			# We have now moved down a row, inc row
			rows += 1
			# If the next row is no longer within this set of windows
			# update the value we update count with, effectively moving zero
			if (rows + 1) % window == 0:
				# increase the incrementor by the amount of windows the can fit on a line
				# |_|_|_|_|  -> inc 4 (4 windows)
				mov = mov +math.ceil(width / window)
		elif (pos + 1) % window == 0:
			# If we are at the edge of a window
			# set new max 
			max[count] = innerMax
			innerMax = 0
			count += 1
	# print("inital loop {} ".format(time.time() - t1))
	
	count = 0
	mov = 0
	rows = 0		
	# t2 = time.time()
	for idx in range(0 , imSize ):
		pos = idx % width
		

		if (pos + 1) % width == 0:
			# print('***\n', im[idx])
			im[idx] = max[count] 
			# print(im[idx], '\n&&&&\n')
			count = mov
			rows += 1
			if (rows + 1) % window == 0:
				mov = mov +math.ceil(width / window)
			continue
		elif (pos + 1) % window == 0:
			# print('8008\n', im[idx])
			im[idx] = max[count] 
			# print(im[idx], '\n$%£\n')
			count += 1
			continue
		# print('8008\n', im[idx])
		im[idx] = max[count] 
		# print(im[idx], '\n$%£\n')
	# print("second loop {}".format(time.time()- t2))
	# print(max)

win =  [[1,     2,     3,     4],
		[11,    22,    33,    44],
		[111,   222,   333,   444],
		[1111,  2222,  3333,  4444],
		[11111, 22222, 33333, 44444]]

# win =  [1,   2,   3,   4,   5,
        # 6,	 7,   8,   9,   10]	

		
# win =  [1,     2,     3,     4,
		# 11,    22,    33,    44,
		# 111,   222,   333,   444,
		# 1111,  2222,  3333,  4444,
		# 11111, 22222, 33333, 44444,
		# 11111, 22222, 33333, 44444,
		# 11111, 22222, 33333, 44444]

		
win = []

# for x in range(0, 1200):
	# for y in range(0, 720):
		# win.append(randint(0,1000))

for x in range(0, 1200):
	tmp = []
	for y in range(0, 720):
		tmp.append(randint(0,1000))
	win.append(tmp)
	
# print("Amount : {}".format(len(win)* len(win[0])))
# pp.pprint(win)
t = time.time()

# slide(win, 3, 720, 1200)
slidingWindow(win, 3)
print("time took : {} ".format(time.time() - t))
# for idx , x in enumerate(win):
	# print(x, end = ', ')
	# if (idx + 1) % 4 == 0:
		# print()
	

