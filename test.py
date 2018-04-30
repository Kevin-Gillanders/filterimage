from PIL import Image
import window
import time
image = Image.open("frymire.png")#.convert('L')
win = 3
minMax = False
width, height = image.size
size = min(width, height)
print(width, height)

t = time.time()

for win in range(1, size):
	px = list(image.getdata())

	red, green, blue = zip(*px)
	red = list(red)
	green = list(green)
	blue = list(blue)

	# print(red)


	# window.slide(px, 3, width, height)
	window.slide(red, win, width, height, minMax)
	window.slide(green, win, width, height, minMax)
	window.slide(blue, win, width, height, minMax)


	px = zip(red, green, blue)
	px = list(px)
	# print(px[0])

	# print(px)

	# for y in range(0, len(px)):
		# print(px[y])
		# px[y] = (px[y][0], 0, 0)
		# px[y] = (0, px[y][1], 0)
		# px[y] = (0, 0, px[y][2])

	image.putdata(px)
	if minMax:
		image.save('./max/' + str(win)+'WindowSize.jpeg', 'jpeg')
	else:
		image.save('./min/' +str(win)+'WindowSize.jpeg', 'jpeg')
	# image.show()

print('it took : {}'.format(time.time()-t))
