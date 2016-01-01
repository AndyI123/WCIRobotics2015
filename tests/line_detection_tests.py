#!/usr/bin/python2

__package__ = "tests"
from lib import *
from cv2 import *
import sys

imagefile = sys.argv[1]

image = imread(imagefile)
imwrite("detected_lines.jpg", line_detection.detectLines(image))