# binary_pix.counter

@created by Adrià Gallifa Terricabras in April 2020 in Crozet, France. During the Covid-19 confinement.

ABSTRACT:
The program measures the distance of black and white regions of a binary image along vertical and horizontal lines, and plots a histogram of the size of the both black and white spots measured, together with its average and standard deviation. 
It was developed to quantify the distance of black and white regions, respectively, in a speckle pattern used for Digital Image Correlation (DIC) development at CERN EN-MME-Materials & Metrology section.
It was developed in Python 3.7.3.

INSTRUCTIONS:
1. Place the three '.py' files and the image that you want to measure in the same directory. The image shall be binary (containing only black and white pixels, or zeros and ones).It works for .PNG and .JPG images.
2. Open the file called 'MAIN_b_w.py'
3. Three inputs are to be entered manually: Image name, number of lines, scale.
Example:
  -image_png='pattern4_.png' #enter the name of the image
  -horiz_lines=50 #enter the number lines in horizontal direction (the number of vertical lines are automatically calculated as             [horizontal lines/aspect ratio])
  -scale=1 #scale in pixels/micron. If you want the measures in pixels, leave it as 1.
4. RUN the program
5. Several results will show up automatically:
·Statistical results in the command line
and
·Three graphs: 
  - the original image with the grid of vertical and horizontal lines used for the measurements.
  - A histogram of the size vs. frequency for black spots, containing the mean and standard deviation values.
  - A histogram of the size vs. frequency for white spots, containing the mean and standard deviation values.
