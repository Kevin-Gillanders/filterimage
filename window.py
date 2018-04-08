import pprint as pp
import time
import numpy as np
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
	pp.pprint(image)
	
	# Segments image into window sized chunks along the x axis
	for y in range(0, len(image), windowSize):
		for x in range(0, len(image[0]), windowSize):
			# print("x : {} y : {} ".format(x, y))
			maximum = 0
			for innerX in range(x, x + windowSize):
				for innerY in range(y, y + windowSize):
					# print(image[innerY][innerX])
					if innerX >= len(image[0]) or innerY >= len(image):
						break
					else:
						# print("x : {} y : {} \nval : {}\n=========".format(innerX, innerY, image[innerY][innerX]))
						maximum = max(maximum, image[innerY][innerX])
			for innerX in range(x, x + windowSize):
				for innerY in range(y, y + windowSize):
					# print(image[innerY][innerX])
					if innerX >= len(image[0]) or innerY >= len(image):
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
	pp.pprint(image)
	
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
	return(fin)

win =  [[1,     2,     3,     4],
		[11,    22,    33,    44],
		[111,   222,   333,   444],
		[1111,  2222,  3333,  4444],
		[11111, 22222, 33333, 44444]]

# win =  [[1,    2,    3,    4],
		# [5,    6,    7,    8]]	

		
# win = []
# for x in range(0, 1280):
	# tmp = []
	# for y in range(0, 720):
		# tmp.append(y)
	# win.append(tmp)
	
# print("Amount : {}".format(len(win)* len(win[0])))
t = time.time()

win = slidingWindow(win, 3)

print("time took : {} ".format(time.time() - t))

# pp.pprint(win)
