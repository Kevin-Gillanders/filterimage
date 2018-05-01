from PIL import Image
import window
import time
import os

print(os.listdir('./testImages'))

for images in os.listdir('./testImages'):
	image = Image.open("./testImages/" + images)#.convert('L')
	win = 3
	minMax = False
	width, height = image.size
	size = min(width, height)
	print(width, height)

	if not (os.path.exists('./max/' + images + '/')):
		os.makedirs('./max/' + images + '/')
	if not(os.path.exists('./min/' + images + '/')):
		os.makedirs('./min/' + images + '/')
		
	t = time.time()
	for both in range(0, 2):
		minMax = not minMax
		for win in range(1, min(100, width, height)):
			image = Image.open("./testImages/" + images)#.convert('L')
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
				image.save('./max/' + images + '/' + str(win)+'WindowSize.jpeg', 'jpeg')
			else:
				image.save('./min/' + images + '/' + str(win)+'WindowSize.jpeg', 'jpeg')
			# image.show()

print('it took : {}'.format(time.time()-t))
