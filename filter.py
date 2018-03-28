from random import randint
import time
from PIL import Image
import numpy as np
import math 


image = Image.open("Jelly_Beans.jpg")#.convert('L')

pix = image.load()[10,10]
pix = [ x / 255 for x in pix]

R = pix[0]
G = pix[1]
B = pix[2]


intensity = (1/3)*sum(pix)
P = [x/(sum(pix)) for x in pix]
# hue = [i/sum(pix)]
top = ((R - G) + (R - B))
bot = 2 * (math.sqrt(math.pow(R - G, 2) + (R-B) * (G - B)) )
hue = math.acos(top/bot)

print("RGB : {}".format(pix))
# print(sum(pix))
print("Intensity : {}".format(intensity))
print("Hue : {}".format(hue))


# image.show()
