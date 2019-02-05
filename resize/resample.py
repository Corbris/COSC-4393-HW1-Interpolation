import cv2
import numpy as np
import math

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using nearest neighbor approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        # Write your code for nearest neighbor interpolation here
        originalHeight, originalWidth = image.shape
        colSize = int(originalWidth * fx)
        rowSize = int(originalHeight * fy)

        newImage = np.ones((rowSize, colSize), np.uint8) * 255  # new blank image

        for x in range(rowSize):
            for y in range(colSize):
                getCol = int(round(originalWidth/colSize*y))
                getRow = int(round(originalHeight/rowSize*x))
                getCol = min(getCol, originalWidth-1)
                getRow = min(getRow, originalHeight-1)

                newImage[x, y] = image[getRow, getCol]

        return newImage





    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        originalHeight, originalWidth = image.shape
        colSize = int(originalWidth * fx)
        rowSize = int(originalHeight * fy)
        newImage = np.ones((rowSize, colSize), np.uint8) * 255  # new blank image


        for r in range(rowSize):
            for c in range(colSize):
                ratioX = 1/fx
                ratioY = 1/fy
                x = c * ratioX
                y = r * ratioY

                x1 = int(c * ratioX) #round down, left of x.
                x2 = min(math.ceil(c * ratioX), originalWidth-1) #round up to next whole, right of x
                y1 = min(math.ceil(r * ratioY), originalHeight-1) #round up to next whole, under of y
                y2 = int(r * ratioY) #round down, top of y

                Q12 = image[int(y2), int(x1)]
                Q22 = image[int(y2), int(x2)]
                Q11 = image[int(y1), int(x1)]
                Q21 = image[int(y1), int(x2)]


                if(x2-x1 == 0):
                    R1 = Q21 #bottem right
                    R2 = Q22 #top right
                elif(x2-x == 0):
                    R1 = Q11 #bottem left
                    R2 = Q12 #top left
                else:
                    R1 = ((x2-x)/(x2-x1))*Q11 + ((x-x1)/(x2-x1))*Q21
                    R2 = ((x2-x)/(x2-x1))*Q12 + ((x-x1)/(x2-x1))*Q22

                if(y2-y1 == 0):
                    P = R2 #top
                elif(y2-y == 0):
                    P = R1 #bottem
                else:
                    P = ((y2-y)/(y2-y1))*R1 + ((y-y1)/(y2-y1))*R2

                newImage[r, c] = P
        return newImage
