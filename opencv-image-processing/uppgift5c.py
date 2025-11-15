from cvlib import greyscale_list_to_cvimg
from cvlib import rgblist_to_cvimg
from cvlib import cvimg_to_list

import random
import cv2
import math




def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Return a function which determines 
    if a pixel is within a ceratin color range.
    """

    def compare_pixel(pixel):
        """
        Compare the pixel inserted as argument, with the
        color range defined above.
        """

        try:
            hue, saturation, value = pixel
            assert isinstance(hue, int)
            assert isinstance(saturation, int)
            assert isinstance(value, int)
            assert 0 <= hue <= 255
            assert 0 <= saturation <= 255
            assert 0 <= value <= 255
        except:
            print("Argument is not a pixel")
            return                               # The function does not raise an error because I wanted
                                                 # to leave room for the possibility of assigning a default
                                                 # value to a corrupted pixel and not stopping the program.

        if ((hlow <= hue <= hhigh) and 
            (slow <= saturation <= shigh) and 
            (vlow <= value <= vhigh)):

            return 1
        
        else:

            return 0
    
    return compare_pixel


def gradient_condition(pixel):
    """
    Return a value between 0 and 1 depending on how
    white a color neutral pixel is with 1 being most
    white and 0 being most black.
    """

    try:
        red, green, blue = pixel
        assert isinstance(red, int)
        assert isinstance(green, int)
        assert isinstance(blue, int)
        assert 0 <= red <= 255
        assert 0 <= blue <= 255
        assert 0 <= green <= 255
    except:
        print("Argument is not a pixel")
        return
        

    if red == green == blue:
        return red/255
    else:
        return 0


def generator_from_image(image_list):
    """
    Take an image as argument and return a function
    which given the index of a pixel returns its color.
    """

    def specific_generator(i):
        """
        Take a pixel index as argument and 
        return the color of it.
        """
        try:
            red, blue, green = image_list[i]
            assert isinstance(red, int)
            assert isinstance(green, int)
            assert isinstance(blue, int)
            assert 0 <= red <= 255
            assert 0 <= blue <= 255
            assert 0 <= green <= 255
        except:
            print("Invalid pixel")
            return

        try:
            return image_list[i]
        except IndexError:
            print("Pixel not in image")
    
    return specific_generator


def star_sky_generator(i):
    """Create a starred sky generator."""

    value = random.random() * 255 if random.random() > 0.99 else 0
    return (value, value, value)


def combine_images(condition_image, condition, generator1, generator2):
    """
    Return a combination of two images which are put in as arguments.
    How the images will be combined is determined by a condition.
    """

    combined_image = []
    for i in range(len(condition_image)):


        try:
            weight = condition(condition_image[i])  # Assign the transparency level between the images in a 
                                                    # specific pixel to a variable.
            assert weight != None

            red1, green1, blue1 = generator1(i)     # Assign the RGB-values of a specific pixel 
                                                    # in the first image to 3 variables.


            red2, green2, blue2 = generator2(i)     # Same but with the second image.
        
        except:
            print("Unable to combine pixel")
            return                                  # The function does not raise an error because I wanted
                                                    # to leave room for the possibility of assigning a default
                                                    # value to a corrupted pixel and not stopping the program.


        combined_red = int(round(red1*weight + red2*(1-weight), 0))         # Create the new combined
        combined_green = int(round(green1*weight + green2*(1-weight), 0))   # values of the pixels
        combined_blue = int(round(blue1*weight + blue2*(1-weight), 0))      # using the weights.
        combined_pixel = (combined_red, combined_green, combined_blue)

        combined_image.append(combined_pixel)                               # Add the new pixel to the
                                                                            # combined image.

    return combined_image






def test_pixel_constraint():
    """Test function for pixel_constraint generator functions."""

    is_black = pixel_constraint(100, 150, 50, 200, 100, 255)
    is_white = pixel_constraint(100, 150, 50, 200, 0, 100)


    assert(is_white((120, 100, 50)) == 1)    # Test a normal positive case.

    assert(is_black((100, 50, 100)) == 1)    # Test a positive case which is 
                                             # on the verge of not being in the interval.

    assert(is_black((120, 0, 150)) == 0)     # Test a negative case with one of the
                                             # values outside the interval.

    assert(is_white((50, 20, 150)) == 0)     # Test a negative case with all of
                                             # values outside the interval.

    assert(is_white(("a", 1, 2)) == None)    # Test exception

    assert(is_white("hej") == None)          # Test another exception

    assert(is_white((1, 2, -1)) == None)     # Another one (outside the pixel interval)

    assert(is_white((1, 2, 300)) == None)    # And another (-||-)



def test_generator_from_image():
    """Test function for generator_from_image."""

    image1 = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]
    image2 = [(250, 25, 100), (255, 43, 89), (55, 67, 200), (125, 179, 200)]

    generator_image1 = generator_from_image(image1)
    generator_image2 = generator_from_image(image2)

    assert(generator_image1(0) != (4, 60, 40))        # Test a normal negative case.

    assert(generator_image2(2) == (55, 67, 200))      # Test a normal positive case.

    assert(generator_image1(10) == None)              # Test exception (index too high).


def test_combine_images():
    """Test function for combine_images."""

    image1 = [(255, 255, 255), (255, 255, 255), (120, 120, 120), (120, 120, 120)]
    image2 = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    image3 = [(0, 0, 1000), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

    generator1 = generator_from_image(image1)
    generator2 = generator_from_image(image2)
    generator3 = generator_from_image(image3)

    gradient_image = [(127, 127, 127), (0, 0, 0), (127, 127, 127), (20, 20, 20)]

    pixel_interval = pixel_constraint(0, 200, 0, 255, 0, 255)

    combined_image1 = [(0, 0, 0), (0, 0, 0), (120, 120, 120), (120, 120, 120)]
    combined_image2 = [(127, 127, 127), (0, 0, 0), (60, 60, 60), (9, 9, 9)]


    # Test a case with pixel_constraint (no gradient):
    assert combine_images(image1, pixel_interval, generator1, generator2) == combined_image1

    # Test a case with gradient_condition:
    assert combine_images(gradient_image, gradient_condition, generator1, generator2) == combined_image2

    # Test an exception (image with one invalid pixel):
    assert combine_images(gradient_image, gradient_condition, generator1, generator3) == None


def test_all():
    """
    Collect all the test functions and print
    "All tests passed" if no AssertionError is
    raised in the tests.
    """

    test_pixel_constraint()
    test_generator_from_image()
    test_combine_images()

    print("All tests passed")


test_all()



#1
"""
hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
plane_list = cvimg_to_list(hsv_plane)

is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)

is_black = pixel_constraint(0, 255, 0, 255, 0, 10)
print(is_black((231, 82, 4)))
print(is_black((231, 82, 80)))
"""

#2
"""
plane_image = cv2.imread("plane.jpg")
plane_list = cvimg_to_list(plane_image)

generator = generator_from_image(plane_list)

new_list = [generator(i) for i in range(len(plane_list))]

cv2.imshow("plane", plane_image)
cv2.imshow("new plane", rgblist_to_cvimg(new_list, plane_image.shape[0], plane_image.shape[1]))
cv2.waitKey(0)

"""

#3
"""
plane_image = cv2.imread("plane.jpg")
plane_list = cvimg_to_list(plane_image)

hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
hsv_plane_list = cvimg_to_list(hsv_plane)

plane_generator = generator_from_image(plane_list)
mask = pixel_constraint(100, 150, 50, 200, 100, 255)

combined_image_list = combine_images(hsv_plane_list, mask, star_sky_generator, plane_generator)
cv2.imshow("combined image", rgblist_to_cvimg(combined_image_list, 
                                              plane_image.shape[0], 
                                              plane_image.shape[1]))
cv2.waitKey(0)
"""

#4
"""
plane_image = cv2.imread("plane.jpg")
plane_list = cvimg_to_list(plane_image)
plane_generator = generator_from_image(plane_list)

flower_image = cv2.imread("flowers.jpg")
flower_list = cvimg_to_list(flower_image)
flower_generator = generator_from_image(flower_list)

gradient_image = cv2.imread("gradient.jpg")
gradient_list = cvimg_to_list(gradient_image)

faded_image_list = combine_images(gradient_list, gradient_condition, plane_generator, flower_generator)
cv2.imshow("faded image", rgblist_to_cvimg(faded_image_list, 
                                           plane_image.shape[0], 
                                           plane_image.shape[1]))
cv2.waitKey(0)

print(gradient_condition((0, 0, 0)))
print(gradient_condition((255, 255, 255)))
print(gradient_condition((128, 128, 128)))
"""



