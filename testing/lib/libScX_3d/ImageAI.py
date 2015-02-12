import numpy

__author__ = 'hc'

#Makes decisions from images

#TODO: Finish this
#THIS IS INCOMPLETE, DO NOT CALL IT
#Determines if an image is processable from a line array
def isSuitable(lines, tkImage):
    lineList = []
    for rho,theta in lines:
        a = numpy.cos(theta)
        b = numpy.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        lineList.append((x1,y1,x2,y2))
