import glob
import numpy as np
from skimage.io import imread, imsave
import sys

# Looking at the first slice to determine array properties
slice_0 = glob.glob('slices/slice00*.png')[0]

# Reading slice_0 as a 2D NumPy array
png_array = imread(slice_0, as_grey=True)

# Initializing 2D output array based on dimensions of slice_0 array
output = np.zeros((len(png_array), len(png_array[0])))
invert_matrix = np.ones((len(png_array), len(png_array[0])))
number_of_slices = 0

# Iterate through each slice in slices folder
for name in glob.glob('slices/slice*.png'):
    number_of_slices += 1

    # Printing progress to terminal
    print_string = "Reading slice: " + name
    print(print_string)

    # Convert png file into 2D array of black/white values
    # black = 0 (min), white = 255 (max)
    png_array = imread(name, as_grey=True)

    # Sum output and current slice array
    output = np.add(output, png_array)

# Normalize the output array (detector)
max_array_value = number_of_slices*255
output = (output/max_array_value)

# Invert image (make black values -> white and vice versa)
# For example, see liver2.bmp (default: black background)
# Uncomment the line below:
# output = invert_matrix - output

# Saving 2D array as bitmap file in output folder
output_file_name = "outputs/" + sys.argv[1] + ".bmp"
imsave(output_file_name, output)
