from PIL import Image
import window

image = Image.open("Jelly_Beans.jpg").convert('L')

width, height = image.size

print(width, height)
px = list(image.getdata())
print(px)

# for y in range(0, width):
	# for x in range(0, height):
		# pix = px[y][x]
		# print(pix)

image.putdata(px)
image.show()