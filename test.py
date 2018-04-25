from PIL import Image
import window
import time
image = Image.open("Jelly_Beans.jpg")#.convert('L')
win = 3
width, height = image.size

print(width, height)

t = time.time()
px = list(image.getdata())



red, green, blue = zip(*px)
red = list(red)
green = list(green)
blue = list(blue)

# print(red)


# window.slide(px, 3, width, height)
window.slide(red, win, width, height)
window.slide(green, win, width, height)
window.slide(blue, win, width, height)


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
image.save(str(win)+'WindowSize.jpeg', 'jpeg')
image.show()

print('it took : {}'.format(time.time()-t))
