import cv2
import numpy as np

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

        print(originalWidth, originalHeight)
        print(colSize, rowSize)

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

        return image
