import math
import numpy


def unsharp_mask(N):
    """
    Return list of lists that can be used as a
    Gaussian blur kernel as a function of the radius N.
    """

    s = 4.5  # Constant of the Gauss function
    p = 1.5  # Value of origo in the kernel

    return ([[p if x == 0 and y == 0 else gauss(s, x, y)
            for x in range((1-N)//2, (N+1)//2)]
            for y in range((1-N)//2, (N+1)//2)])


def gauss(s, x, y):
    """
    Return offset of the pixel located in a specific coordinate.
    """

    return (-(1/(2*math.pi*s**2)))*(math.e**(-(x**2+y**2)/(2*s**2)))


print(unsharp_mask(3))


"""
import cv2
import cvlib

filename = "fruit.jpg"
image = cv2.imread(filename, 1)
kernel = numpy.array(unsharp_mask(11))
filtered_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("unfiltered", image)
cv2.imshow("filtered", filtered_image)
cv2.waitKey(0)
"""
