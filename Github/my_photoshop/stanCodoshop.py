"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: This program allows users to remove people in a series of pictures with the same scenery.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2) ** (1/2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # Variables to derive the average of different pixel color values
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    red_num = 0
    green_num = 0
    blue_num = 0

    # Loop through each pixel in the list
    for pixel in pixels:
        if pixel.red > 0:                                                   # add up the value and the number
            red_sum += pixel.red
            red_num += 1
        if pixel.green > 0:
            green_sum += pixel.green
            green_num += 1
        if pixel.blue > 0:
            blue_sum += pixel.blue
            blue_num += 1

    # Compute the average for each color value
    if red_num == 0:                                                        # check whether none of pixels has the color
        red_avg = 0
    else:                                                                   # if not, divide the sum with the number
        red_avg = red_sum/red_num
    if green_num == 0:
        green_avg = 0
    else:
        green_avg = green_sum/green_num
    if blue_num == 0:
        blue_avg = 0
    else:
        blue_avg = blue_sum/blue_num

    # Return the list of average color values
    rgb = [red_avg, green_avg, blue_avg]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # Variables to derive the best distance
    avg = get_average(pixels)
    red_avg = avg[0]                                                        # color averages
    green_avg = avg[1]
    blue_avg = avg[2]
    best_dist = get_pixel_dist(pixels[0], red_avg, green_avg, blue_avg)     # the first pixel is the best so far
    best = pixels[0]

    # Loop through each pixel in the list
    for pixel in pixels:
        if get_pixel_dist(pixel, red_avg, green_avg, blue_avg) < best_dist:
            best = pixel                                                    # update the best pixel if it's closer
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    # Loop through each pixel in the blank picture
    for x in range(result.width):
        for y in range(result.height):

            # Gather pixels with the same coordinate but in different images in a list
            img_lst = []
            for img in images:
                pixel = img.get_pixel(x, y)
                img_lst.append(pixel)

            # Get the best(closest) among all pixels and use it in the blank picture
            best = get_best_pixel(img_lst)
            result_pixel = result.get_pixel(x, y)                           # coordinate for the blank picture
            result_pixel.red = best.red                                     # assign different color values
            result_pixel.green = best.green
            result_pixel.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
