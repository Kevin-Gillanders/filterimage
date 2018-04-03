import pprint as pp
import time
# def chunks(l, n): 
	# for i in range(0, len(l), n):
		# return l[i:i + n]

		
def slidingWindow(image, windowSize):
	# pp.pprint(image)
	tmp = []
	# Segments image into window sized chunks along the x axis
	for idx, row in enumerate(image):
		tmp = []
		for x in range(0, len(row), windowSize):
			tmp.append(row[x:x + windowSize])
		image[idx] = tmp
	tmp = []
	size = len(image)
	# pp.pprint(image)
	fin = []
	# merges chunks along the y axis 
	for x in range(0, len(image), windowSize):
		# tmp.append(image[row])
		fin.append(zip(*image[x:x + windowSize]))
		# if (row + 1) % windowSize == 0:
			# print(list(zip(*tmp)))
			# fin.append(tmp)	
			# tmp = []
		# print(image[row])
	# for x in fin:
		# for y in x : 
			# pp.pprint(y)
	# pp.pprint(zip(*image))
	return(fin)

# win =  [[1,     2,     3,     4],
		# [11,    22,    33,    44],
		# [111,   222,   333,   444],
		# [1111,  2222,  3333,  4444],
		# [11111, 22222, 33333, 44444]]
win = []
for x in range(0, 1280):
	tmp = []
	for y in range(0, 720):
		tmp.append(y)
	win.append(tmp)
	
print("Amount : {}".format(len(win)* len(win[0])))
t = time.time()

win = slidingWindow(win, 3)

print("time took : {} ".format(time.time() - t))

# pp.pprint(win)
