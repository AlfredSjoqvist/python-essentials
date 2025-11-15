import cv2
import cvlib

filename = "fruit.jpg"
image = cv2.imread(filename, 1)


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


pixel_list = cvimg_to_list(image)
converted_image = cvlib.rgblist_to_cvimg(pixel_list,
                                         image.shape[0], image.shape[1])

cv2.imshow("Before conversion", image)
cv2.imshow("Converted back and forth", converted_image)
cv2.waitKey(0)
