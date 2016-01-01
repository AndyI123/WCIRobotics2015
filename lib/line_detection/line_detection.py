# Line detection module
# Uses OpenCV's Hough Transform function to detect lines in an image.
# Authors:
# - Alexander Kitaev

from cv import *
from cv2 import *
import cv2
import numpy

__package__ = "lib"

THRESHOLD = 250
# NOTE: This 'threshold' is effectively the minimum length of line to be detected.
# This should be changed as needed, _and will probably be_.

# detectLines(image) -> lines
# image: normal image variable. Need not be grayscale- the function automatically converts it.

def detectLines(image):
	result = image
	grayScaleImage = cvtColor(image, COLOR_BGR2GRAY)
	edges = cv2.Canny(grayScaleImage, threshold1 = 300, threshold2 = 300, apertureSize = 3)
	lines = cv2.HoughLines(edges, 1, (CV_PI / 180), 200)
	if lines is None:
		return None
	for rho, theta in lines[0]:
		a = numpy.cos(theta)
		b = numpy.sin(theta)
		x0 = a * rho
		y0 = b * rho
		# The next four lines find the endpoints of the line.
		x1 = int(x0 - 1000 * b)
		x2 = int(x0 + 1000 * b)
		y1 = int(y0 + 1000 * a)
		y2 = int(y0 - 1000 * a)
		line(result, (x1, y1), (x2, y2), (255, 0, 0), 2)
		# NOTE: In the above function call, the fourth parameter is a tuple
		# representing the BGR (not RGB, BGR!) code of the color: this is blue.
	return result
