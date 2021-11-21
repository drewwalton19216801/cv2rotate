#!/usr/bin/python3
import datetime
import cv2
import argparse
import sys, os

"""Function to parse the following arguments:
    1: Verbose mode (-v or --verbose), Run in verbose mode.
    2: Input image file path (-i or --image), Path to the original image.
    3: Output image file path (-o or --output), Path to the new image. Not required if benchmark mode is on.
    4. Rotation vector (-r or --rotate), Rotation percentage amount.
    5. Benchmark mode (-b or --benchmark), Run in benchmark mode. Not required.
    6. Force overwriting (-f or --force), Force overwriting. Not required."""
def parse_args():
    parser = argparse.ArgumentParser(description='Rotate an image.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Run in verbose mode.')
    parser.add_argument('-i', '--image', required=True, help='Path to the original image.')
    parser.add_argument('-o', '--output', help='Path to the new image. Not required if benchmark mode is on.')
    parser.add_argument('-r', '--rotate', required=True, help='Rotation percentage amount.')
    parser.add_argument('-b', '--benchmark', action='store_true', help='Run in benchmark mode.')
    parser.add_argument('-f', '--force', action='store_true', help='Force overwriting.')
    return parser.parse_args()

def rotate_image(image, angle):
    """Rotate an image by the given angle."""
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def benchmark(image, angle):
    """Benchmark the rotation process 1000 times"""
    start = datetime.datetime.now()
    for i in range(1000):
        rotate_image(image, angle)
    end = datetime.datetime.now()
    return end - start

args = parse_args()
"""If benchmark mode is off, check if the output file has been specified"""
if not args.benchmark:
    if args.output is None:
        print("Error: No output file specified.")
        sys.exit(1)
else:
    """Run the benchmark"""
    print("Benchmarking by rotating 1000x...")
    image = cv2.imread(args.image)
    angle = int(args.rotate)
    print("Rotation angle: {}".format(angle))
    print("Time taken: {}".format(benchmark(image, angle)))
    sys.exit(0)

"""Inform the user if verbose mode is on"""
if args.verbose:
    print('Verbose mode is on')
    """Print the start date and time"""
    print('Started at {}'.format(datetime.datetime.now()))

"""Read the image file to be processed"""
image = cv2.imread(args.image)
"""If verbose mode is on, inform the user that we have loaded the image"""
if args.verbose:
    print('Loaded image {}'.format(args.image))
    """Also inform the user of the image shape"""
    print('Image shape: {}'.format(image.shape))

"""If verbose mode is on, inform the user that we are rotating the image by the given angle at the current time"""
if args.verbose:
    print('Rotating image by {}% at {}'.format(args.rotate, datetime.datetime.now()))    

"""Rotate the image by the given angle"""
rotated = rotate_image(image, int(args.rotate))

"""If verbose mode is on, inform the user that we have rotated the image by the given angle at the current time"""
if args.verbose:
    print('Rotated image by {}% at {}'.format(args.rotate, datetime.datetime.now()))
    """Also inform the user of the image shape"""
    print('Image shape: {}'.format(rotated.shape))

"""If force mode is off, check if the file already exists"""
if not args.force:
    if os.path.exists(args.output):
        """If the file already exists, inform the user and exit"""
        print('Output file already exists. Use -f or --force to overwrite.')
        sys.exit(1)
else:
    """Tell the user that the output file already exists, but we are proceeding anyway because force mode is on."""
    print('Output file already exists. Force mode is on. Overwriting.')

"""If verbose mode is on, inform the user that we are saving the image"""
if args.verbose:
    print('Saving image {}'.format(args.output))

"""Save the rotated image"""
cv2.imwrite(args.output, rotated)

"""Inform the user that we have saved the new image, and tell them where the new image is saved."""
print('Saved image {}'.format(args.output))

"""If verbose mode is on, print the finish date and time"""
if args.verbose:
    print('Finished at {}'.format(datetime.datetime.now()))

"""Exit the program"""
exit(0)
