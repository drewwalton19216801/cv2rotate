# cv2rotate
Arbitrary image rotation using OpenCV2 and Python

## Usage
```
usage: cv2rotate.py [-h] [-v] -i IMAGE [-o OUTPUT] -r ROTATE [-b BENCHMARK] [-f]

  -h, --help            show this help message and exit
  -v, --verbose         Run in verbose mode.
  -i IMAGE, --image IMAGE
                        Path to the original image.
  -o OUTPUT, --output OUTPUT
                        Path to the new image. Not required if benchmark mode is on.
  -r ROTATE, --rotate ROTATE
                        Rotation percentage amount.
  -b BENCHMARK, --benchmark BENCHMARK
                        Benchmark the rotation N times.
  -f, --force           Force overwriting.
```

cv2rotate.py allows for arbitrary rotating of images using the OpenCV2 library.

It supports a benchmarking mode that rotates an image (-i, --image) by the user-specified number of degrees (-r, --rotate). A single run (-b 1) of the benchmark performs the rotation 1000 times.

99% of the code was generated from comments by GitHub Copilot.
