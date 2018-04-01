from random import randint
import time
from PIL import Image
import numpy as np
import math 


def getHue(R, G, B, cmax, cmin, delta):
	if delta == 0:
		return(0)
	elif cmax == R:
		return(60 * (((G - B) / delta) % 6))
	elif cmax == G:
		return(60 * (((B - R) / delta) + 2))
	else:
		return(60 * (((R - G) / delta) + 4))

		
def getHSLLuminance(cmax, cmin):
	return(cmax + cmin)*(1/2)
		
		
def getHSLSaturation(max, min, luminance):
	if max ==  min:
		return(0)
	elif luminance <= 0.5:
		return ((max - min) / (2 * luminance))
	else:
		return ((max - min) / (2 - (2 * luminance)))
# return(delta / (1 - abs((2 * luminance) - 1)))


def getHSVSaturation(delta, cmax):
	if cmax != 0:
		return(delta / cmax)
	return(0)

	
def getHSIHue(R, G, B):
	# print(1)
	top = (R - G) + (R - B)
	bot = math.pow( (math.pow((R - G), 2) + ((R - B)*(G - B))) , 0.5)
	# print(2)
	# print("RGB {} , {} , {}".format(R, G, B) )
	# print("top : ", top)
	# print("bot : ", bot)
	
	val = top / bot
	if val > 1:
		val = 1.0
	elif val < -1:
		val = -1.0
	h =  math.acos( val) 
	
	if B > G:
		h = 360 - h
	return h
	
def getHSIIntensity(R, G, B):
	return (R + G + B)/3


def getHSISaturation(R, G, B, intensity):
	return 1 - (3 / (R + G + B) * min(R, B, G))
	
		
def RGBtoHSL(pix):		
	pix, R, G, B, cmax, cmin, delta = getVariables(pix)
	
	hue = getHue(R, G, B, cmax, cmin, delta)
	luminance = getHSLLuminance(cmax, cmin)
	saturation = getHSLSaturation(cmax, cmin, luminance)
	
	return((hue, saturation, luminance))

	
def RGBtoHSV(pix):
	pix, R, G, B, cmax, cmin, delta = getVariables(pix)

	hue = getHue(R, G, B, cmax, cmin, delta)
	saturation = getHSVSaturation(delta, cmax)
	value = cmax
	
	return((hue, saturation, value))
	

def RGBtoHSI(pix):
	pix, R, G, B, cmax, cmin, delta = getVariables(pix)
	
	intensity = getHSIIntensity(R, G, B)
	hue = getHSIHue(R,G,B)
	saturation = getHSISaturation(R,G,B, intensity)
	
	return((hue, saturation, intensity))
	
def getVariables(pix):
	pix = [ x / 255 for x in pix]

	R = pix[0]
	G = pix[1]
	B = pix[2]

	cmax = max(pix)
	cmin = min(pix)
	delta = cmax - cmin
	
	return(pix, R, G, B, cmax, cmin, delta)

	
def getColours(h, c, x, m):
	R = 0
	G = 0
	B = 0
	
	if h >= 0 and h < 60:
		R, G, B = (c, x, 0)
	elif h >= 60 and h < 120:
		R, G, B = (x, c, 0)
	elif h >= 120 and h < 180:
		R, G, B = (0, c, x)
	elif h >= 180 and h < 240:
		R, G, B = (0, x, c)
	elif h >= 240 and h < 300:
		R, G, B = (x, 0, c)
	elif h >= 300 and h < 360:
		R, G, B = (c, 0, x)
	
	return ((R + m) * 255, (G + m) * 255, (B + m) * 255)
	

def HSLtoRGB(hsl):
	h = hsl[0]
	if h == 0:
		h += 0.01
	s = hsl[1]
	l = hsl[2]
	
	c = (1 - abs(2 * l - 1)) * s
	x = c * (1 - abs((h / 60) % 2 - 1))
	m = l - c/2
	
	R = 0
	G = 0
	B = 0
	
	# if h >= 0 and h < 60:
		# R, G, B = (c, x, 0)
	# elif h >= 60 and h < 120:
		# R, G, B = (x, c, 0)
	# elif h >= 120 and h < 180:
		# R, G, B = (0, c, x)
	# elif h >= 180 and h < 240:
		# R, G, B = (0, x, c)
	# elif h >= 240 and h < 300:
		# R, G, B = (x, 0, c)
	# elif h >= 300 and h < 360:
		# R, G, B = (c, 0, x)
	
	# return ((R + m) * 255, (G + m) * 255, (B + m) * 255)
	return getColours(h, c, x, m)

	

def HSVtoRGB(hsv):
	h = hsv[0]
	if h == 0:
		h += 0.01
	s = hsv[1]
	v = hsv[2]
	

	c = v * s
	x = c * (1 - abs((h / 60) % 2 - 1))
	m = v - c
	
	return getColours(h, c, x, m)


def HSItoRGB(hsi):
	h = hsi[0]
	if h == 0:
		h += 0.01
	s = hsi[1]
	i = hsi[2]

	h *= 360        
	##        s *= 100
	##        i *= 255

	h = h * math.pi / 180    
	# print(h)



	if h < 2 * math.pi / 3:
		# print(1)
		x = i * (1 - s)
		y = i * (1 + ((s * math.cos(h)) / math.cos(math.pi / 3 - h)))
		z = 3 * i - (x + y)    
		
		b = x
		r = y 
		g = z
	elif h >= 2 * math.pi / 3 and h < 4 * math.pi / 3:
		# print(2)
		h = h - 2 * math.pi / 3
	
		x = i * (1 - s)
		y = i * (1 + ((s * math.cos(h)) / math.cos(math.pi / 3 - h)))
		z = 3 * i - (x + y)    

		r = x 
		g = y
		b = z
	elif h >= 4 * math.pi / 3: #and h < 2 * math.pi:
		# print(3)
		h = h - 4 * math.pi / 3
		
		x = i * (1 - s)
		y = i * (1 + ((s * math.cos(h)) / math.cos(math.pi / 3 - h)))
		z = 3 * i - (x + y)    

		g = x
		b = y
		r = z
	##	if h > 0 and h <= 120:
	##		h = 0 
	##		r = i * ( (1 + (s * math.cos(h))) / (math.cos(60 - h)) )
	##		b = i - i * s
	##		g = 3 * i - r - b
	##	elif h > 120 and h <= 240:
	##		h = h - 120
	##		r = i - i * s
	##		g = i * ( (1 + (s * math.cos(h))) / (math.cos(60 - h)) )
	##		b = 3 * i - r - g
	##	elif h > 240 and h <= 360:
	##		h = h - 240
	##		g = i - i * s
	##		b = i * ( (1 + (s * math.cos(h))) / (math.cos(60 - h)) )
	##		r = 3 * i - b - g


	return (r*255, g*255, b*255)

	
def breakdownImage(im, width, height):
	pixels = image.load()
	
	hslIm = []  
	hsvIm = [] 
	hsiIm = []
	hslrgbIm = []
	hsvrgbIm = [] 
	hsirgbIm = []
	
	for y in range(0, width):
		for x in range(0, height):
			pix = pixels[y, x]
		
			hslIm.append( RGBtoHSL(pix))
			hsvIm.append( RGBtoHSV(pix))
			hsiIm.append( RGBtoHSI(pix))
	#TODO decide if this should be 1D of multi dim
	hslrgbIm = list(map(HSLtoRGB, hslIm))
	hsvrgbIm = list(map(HSVtoRGB, hsvIm))
	hsirgbIm = list(map(HSItoRGB, hsiIm))
	
	return hslIm, hsvIm, hsiIm, hslrgbIm, hsvrgbIm, hsirgbIm

	
image = Image.open("Jelly_Beans.jpg")#.convert('L')

width, height = image.size

print(width, height)
px = image.load()

hslIm, hsvIm, hsiIm, hslrgbIm, hsvrgbIm, hsirgbIm = breakdownImage(image, width, height )
# count = 0 
# with open('hsltest.txt', 'w') as r:
	# for x, y in zip(hsiIm, hsirgbIm):
		# r.write("{}\n{}\n{}\n=========\n".format(x, y, px[0, count % width]))
		# print(px[count % height, count % width], count)
		# count += 1
		# if count == 200:
			# break
window = 0

print(window)
# for idx, x in enumerate(hsvrgbIm):
	
	

		
# print(hslIm)
# print()


# print("RGB : {}\n".format(pix))


# print("Hue : {}\nSaturation : {}\nValue : {}\n".format(*hsv))
# print("HSV to RGB : {}\n".format(hsvrgb))


# print("Hue : {}\nSaturation : {}\nLuminence : {}\n".format(*hsl))
# print("HSL to RGB : {}\n".format(hslrgb))


# print("Hue : {}\nSaturation : {}\nIntensity : {}".format(*hsi))
# print("HSI to RGB : {}\n".format(hsirgb))



# hue = [i/sum(pix)]
# top = ((R - G) + (R - B))
# bot = 2 * (math.sqrt(math.pow(R - G, 2) + (R-B) * (G - B)) )
# hue = math.acos(top/bot)

# print(sum(pix))
# print("Hue : {}".format(hue))


# image.show()
