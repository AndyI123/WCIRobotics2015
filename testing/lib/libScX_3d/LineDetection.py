import numpy
import cv2
from cv2.cv import CV_BGR2GRAY, CV_PI

__author__ = 'hc'

#A line detection implementation that auto-adjusts thresholds and sensitivities!

#Main line detection code:
#Arguments:
#src: The source image, can be in color if needed
#threshold: This is the master threshold, it controls the optimal number of lines detected
#cannyThreshold1: This is the starting Canny Threshold1, it is auto adjusted (You shouldn't touch this)
#cannyThreshold2: This is the starting Canny Threshold2, it is auto adjusted (You shouldn't touch this)
#houghLinesThreshold: This is the HoughLines Threshold, it is constant, change it if you want...
#startingSensitivity: This is the starting sensitivity, you shouldn't touch it... (It's also backwards)
def detectLines(src, threshold=5, cannyThreshold1=100, cannyThreshold2=100, houghLinesThreshold=200, startingSensitivity=100):

    #Some other variables...
    linesFound = 0
    thresholdFound = False
    newCannyThreshold1 = cannyThreshold1
    newCannyThreshold2 = cannyThreshold2
    sensitivity = startingSensitivity

    #================[Actual Code]================#

    while thresholdFound != True:
        edges = cv2.Canny(cv2.cvtColor(src, CV_BGR2GRAY), threshold1=newCannyThreshold1, threshold2=newCannyThreshold2,apertureSize = 3)
        lines = cv2.HoughLines(edges,1,CV_PI/180,houghLinesThreshold)

        errorFound = False
        try:
            #Count the lines
            for rho,theta in lines[0]:
                linesFound = linesFound + 1

        except (TypeError):
            #No lines found so more sensitivity please...
            errorFound = True
            if(sensitivity <= 10):
                print "Sensitivity too low to adjust further, aborting..."
                errorFound = True
                thresholdFound = True
            else:
                #Increase sensitivity
                print "Sensitivity too low! Increasing sensitivity by 10 (new sensitivity is: " + str(sensitivity) + ")"
                sensitivity = sensitivity - 10 #The "-" here is not a mistake, the sensitivity is backwards...
                newCannyThreshold1 = cannyThreshold1
                newCannyThreshold2 = cannyThreshold2

        if linesFound <= threshold and errorFound == False:
            thresholdFound = True
            print "Jackpot buddy, we've got the right amount of lines: " + str(linesFound)

            #WE ARE DONE :)
            return lines[0]
        else:
            if errorFound == False:
                print "Too many lines (" + str(linesFound) + ") continuing search!"
                newCannyThreshold1 = newCannyThreshold1 + sensitivity
                newCannyThreshold2 = newCannyThreshold2 + sensitivity
                linesFound = 0

def writeLinesToImage(lines,imgData):
    newImgData = imgData
    if lines is None:
        return imgData
    for rho,theta in lines:
        a = numpy.cos(theta)
        b = numpy.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(newImgData,(x1,y1),(x2,y2),(0,0,255),2)
    return newImgData