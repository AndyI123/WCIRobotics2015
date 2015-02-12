import os
import PIL
import cv2

__author__ = 'hc'

#Deals with pictures :/

#Reads an image into cv2
#Arguments:
#path: The path of the image
def readCV2Image(path):
    src = cv2.imread(path)

    #Get file extension
    nothingHeretoUse, extension = os.path.splitext(path)

    return src, extension

#Writes an image to disk
#Arguments:
#path: The path to the output file
def writeCV2Image(imgData, path):
    cv2.imwrite( path, imgData );

def readTKImage(path):
    image = PIL.Image.open(path)

    #Get file extension
    nothingHeretoUse, extension = os.path.splitext(path)

    return image, extension

#Arguments:
#imgData: The OpenCV image data
#targetBGR1: The first RGB of the target color range
#targetBGR2: The second RGB of the target color range
#Example: filterImage(imgData, (255,255,255), (0,0,0))
#WARNING THE NUMBERS IN targetBGR1 SHOULD ALWAYS BE BIGGER THAT THE NUMBERS IN targetBGR2
def filterImage(imgData, targetBGR1, targetBGR2, foregroundColor=None, backgroundColor=(0,0,0)):
    outImgData = imgData
    rows, cols, somethingUseless = outImgData.shape
    for x in range(0,rows-1):
        for y in range(0,cols-1):
            tB1, tG1, tR1 = targetBGR1
            tB2, tG2, tR2 = targetBGR2
            inRange = False
            #Why numpy? OpenCV says it's faster: http://goo.gl/2GyEgQ
            if tB2 <= outImgData.item(x,y,0) <= tB1:
                if tG2 <= outImgData.item(x,y,1) <= tG1:
                    if tR2 <= outImgData.item(x,y,2) <= tR1:
                        inRange = True
                        if foregroundColor is not None:
                            b,g,r = foregroundColor
                            outImgData.itemset((x,y,0),b)
                            outImgData.itemset((x,y,1),g)
                            outImgData.itemset((x,y,2),r)
            if not inRange:
                b,g,r = backgroundColor
                outImgData.itemset((x,y,0),b)
                outImgData.itemset((x,y,1),g)
                outImgData.itemset((x,y,2),r)
    return outImgData
