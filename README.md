# cv2rotate
Arbitrary image rotation using OpenCV2 and Python

## Usage
```
usage: cv2rotate.py [-h] [-v] -i IMAGE [-o OUTPUT] -r ROTATE [-b] [-f]

-h, --help: Displays help text
-v, --verbose: verbose mode shows additional debugging messages
-i, --image: Path to the image you wish to rotate.
-o, --output: Path to where you want to save the rotated image. Not required when benchmarking.
-r, --rotate: An arbitrary rotation percentage (whole numbers, 0-360)
-b, --benchmark: Runs the benchmark
-f, --force: Forces overwriting the output file if the file already exists.
```

cv2rotate.py allows for arbitrary rotating of images using the OpenCV2 library. It supports a rudimentary benchmarking mode that simply rotates an image (-i, --image) by the user-specified number of degrees (-r, --rotate) in memory 1000 times.
