"""cvlib module, helper functions for image and tuple manipulation."""

import cv2
import numpy

# ------------------------------------------
#  Helper functions
# ------------------------------------------

def cvimg_to_list(image):
    """
    Takes an OpenCV image object as argument
    and returns a list with the pixels as tuples.
    """

    list_of_pixels = []

    height, width = image.shape[0], image.shape[1]

    # Iterate through every pixel and put the color values in a new tuple:
    for y in range(height):
        for x in range(width):
            blue = image[y, x][0]
            green = image[y, x][1]
            red = image[y, x][2]
            list_of_pixels.append((blue, green, red))

    return list_of_pixels


def multiply_tuple(tpl, mult):
    """Return a tuple where all elements are scaled by factor 'mult'.

    (a,b,c) * k = (a*k, b*k, c*k)
    """
    return tuple(map(lambda x: x*mult, tpl))


def add_tuples(tpl1, tpl2):
    """
    Return a the element-wise sum of tpl1 and tpl2.

    (a,b,c) + (d,e,f) = (a+d, b+e, c+f)
    """
    return tuple(map(lambda t1, t2: t1+t2, tpl1, tpl2))


# -------------------------------------------
#  Converting between python list and images
# -------------------------------------------


def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img


def greyscale_list_to_cvimg(lst, height, width):
    """Return a width x height grayscale OpenCV image with specified pixels."""
    img = numpy.zeros((height, width), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            img[y, x] = lst[y * width + x]

    return img
