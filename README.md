# X-Ray Simulator
Turns an ASCII STL file into its x-ray simulation as bitmap image

<img height="200" alt="Stanford Bunny STL representation" src="https://user-images.githubusercontent.com/12778335/67732785-b906b000-f9b9-11e9-8373-436e66ab5b0a.png"> |  <img height="200" alt="Stanford Bunny x-ray representation" src="https://user-images.githubusercontent.com/12778335/67732754-a12f2c00-f9b9-11e9-829b-fec4af42f134.png">
:------------------------------------------------------------:|:---------------------------------------------------------------------------:


## Input
* ASCII STL file
* FILENAME should correspond to the name of the file (without the .stl extension)
* For HalfDonut.stl, FILENAME = HalfDonut
* All inputs must be located in inputs folder

## Output
* Bitmap file in the outputs folder titled FILENAME.bmp
* All outputs will be placed in outputs folder
* Corresponding inputs and outputs will have the same name (FILENAME)

## Requirements
* Install dependencies:
> pip install -r requirements.txt

## How to Run
> bash xray_simulator.sh $FILENAME

##### Examples
* All tested examples can be found in the inputs and outputs folders
* Corresponding inputs and outputs have the same file name


## Implementation
* Bash script xray_simulator.sh runs 2 different programs: stl-to-voxel and sum_slices
* Bash script removes files in slices folder before running programs

##### stl-to-voxel (third-party open-source library):
* Purpose: Simulating light rays on each slice
* Access STL file in inputs folder
* Convert STL file into voxels, represented as a series of PNG images (slices), in the slices folder

##### sum_slices:
* Purpose: Getting the detector output
* Convert PNG files (slices) into 2D arrays
* 2D array representation: if a value at row i and column j has a value of 255, then that pixel will be white; if i,j has a value of 0, then the pixel will be black
* Sum up each slice array as the detector would see it
* Divide final output by the maximum value the output array can have (255*(number of slices))
* By default, image has black background and white object; to invert, uncomment line in sum_slices.py (see example of inverted image - liver2.bmp)
* Convert output matrix into bitmap file
* Save bitmap file to outputs folder

## Assumptions
* Object in STL file is made up of the same material throughout
* Uniform density and material properties for the entire object
* Light hits all slices evenly and all slices have an equal effect on the final result
* X-ray image is a function of how 'dense' the object is at that point
* If there is an object at a particular slice and pixel, then that means that pixel will have a greater white output
* It is possible to sum slices to get overall density output


## Libraries Used
##### stl-to-voxel (https://github.com/rcpedersen/stl-to-voxel)
* Turns STL files into voxels, represented as PNGs
* This program may use its own third-party libraries

##### NumPy (http://www.numpy.org/)
* For faster mathematical operations (matrix addition)

##### scikit-image (http://scikit-image.org/)
* To read PNG files as 2D NumPy arrays
* To output 2D NumPy arrays as bitmap images


## Limitations and Errors
* Cannot select the rotation of STL object
* Bitmap resolution is 102x102


## Future Extensions
* Select the rotation of STL object
* Change bitmap output for higher resolution
* Figure out sources of error in library used
* Voxelize STL files without third-party library
* Implement light source as a point
* Account for light going straight through or bouncing off objects
* Improve contrast ratio on some images


## Sources for Sample STL Files
* Half Donut: https://github.com/WoLpH/numpy-stl/tree/develop/tests/stl_ascii
* Teapot: https://clara.io/view/8d9a8181-f1ce-4340-b24f-e36bbaf318f7
* Bunny: https://clara.io/view/616bf87b-c7f2-4925-b0d5-688069aee331
* Plane Chassis: https://clara.io/view/baf8fd3b-a91b-49bb-84d8-5cfba6128fc3
* Wheel: https://clara.io/view/1cab45be-7f55-42c9-9c6a-44685224a917
* Rubix Cube: https://clara.io/view/c703d22e-7cae-45bb-aa22-1f7dbb230fde
* Liver (Liver2 is the same file): http://people.sc.fsu.edu/~jburkardt/data/stla/stla.html
* Antenna and Steering Wheel: https://clara.io/view/67671352-3f28-4028-b7cc-3e1aa5222663
