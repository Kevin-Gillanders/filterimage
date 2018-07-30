# Pixelate image

This is a small image processing program which will pixelate an image using min or max filter as detailed [here](https://www.nayuki.io/page/sliding-window-minimum-maximum-algorithm)

## Prerequisites
A python 3 environment

## Run
To run the project all you have to do is download the repo and run test.py

This will then : 
1. Go into the testImages folder
2. Cycle through all images in the folder
3. Generating fully, a full min and max series, increasing pixelation by 1 each time
4. The pixelated pictures will be placed in their corresponding folder in the min and max folders

## Filters 

The filters Minimun and maximum, iterate over all pixels in the image in a window. This window size can be increased for increased pixelation.

The filter selects the smallest and largest value in the window, respectively, in red, green and blue.
The maximum filter favours lighter colours (e.g. white and yellow). Whereas the minimum filter favours dark colours such as black.

This seems a litte unintuitive, but once we look into how RBG (works)[https://www.w3schools.com/colors/colors_rgb.asp] it makes perfect sense.

## Examples

### Cat
**Original cat, no filter**

![Cat, no filter](https://github.com/Kevin-Gillanders/filterimage/blob/master/examples/max/cat.png/1WindowSize.jpeg)

**cat, 10 max pixel window**

![Cat, no filter](https://github.com/Kevin-Gillanders/filterimage/blob/master/examples/max/cat.png/10WindowSize.jpeg)


**cat, 24 max pixel window**

![Cat, no filter](https://github.com/Kevin-Gillanders/filterimage/blob/master/examples/max/cat.png/24WindowSize.jpeg)


**cat, 10 min pixel window**

![Cat, no filter](https://github.com/Kevin-Gillanders/filterimage/blob/master/examples/min/cat.png/10WindowSize.jpeg)


**cat, 24 min pixel window**

![Cat, no filter](https://github.com/Kevin-Gillanders/filterimage/blob/master/examples/min/cat.png/24WindowSize.jpeg)
