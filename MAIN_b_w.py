# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:50:52 2020

@author: adria
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageDraw
from count_bw_array import count_bw_array
from measure_bw_image import measure_bw_image
plt.close('all')

###INPUTS###
image_png='pattern1.png'
horiz_lines=50 #enter the number of lines per direction
#vert_lines=2 #remove comment to use independent vert vs. horiz lines
scale=1 #in pixels/micron

###CALL FUNCTIONS###
img = mpimg.imread(image_png)
aspect_ratio=img.shape[0]/img.shape[1]
vert_lines=round(horiz_lines/aspect_ratio) #put comment to use independent horiz and vert lines!!!
L_x_all_b,L_x_all_w,arr_x_b,arr_x_w,L_y_all_b,L_y_all_w,arr_y_b,arr_y_w, x_,y_= measure_bw_image(image_png,vert_lines,horiz_lines)

###CALCULATIONS###
#divide the flatened arrays by the scale. Put comment in front if pixels is fine.
arr_x_b=arr_x_b/scale
arr_x_w=arr_x_w/scale
arr_y_b=arr_y_b/scale
arr_y_w=arr_y_w/scale

length_vert_lines=vert_lines*(img.shape[0])/scale
length_horiz_lines=horiz_lines*(img.shape[1])/scale

N_x_b=len(arr_x_b)
N_x_w=len(arr_x_w)
N_y_b=len(arr_y_b)
N_y_w=len(arr_y_w)

avg_x_b=np.mean(arr_x_b)
avg_x_w=np.mean(arr_x_w)
avg_y_b=np.mean(arr_y_b)
avg_y_w=np.mean(arr_y_w)

std_x_b=np.std(arr_x_b)
std_x_w=np.std(arr_x_w)
std_y_b=np.std(arr_y_b)
std_y_w=np.std(arr_y_w)

array_all_black=np.concatenate((arr_x_b, arr_y_b), axis=None)
array_all_white=np.concatenate((arr_x_w, arr_y_w), axis=None)
N_all_b=len(array_all_black)
N_all_w=len(array_all_white)
N_all=N_all_b+N_all_w
length_black_spots=sum(array_all_black)
length_white_spots=sum(array_all_white)
tot_length=length_black_spots+length_white_spots

avg_black=round(np.mean(array_all_black),2)
avg_white=round(np.mean(array_all_white),2)
std_black=round(np.std(array_all_black),2)
std_white=round(np.std(array_all_white),2)

#PRINTS
print()
if scale==1:
    print('\033[4m'+'RESULTS (units in PIXELS):'+'\033[0m')
else:
    print('RESULTS --- units in MICRONS:')
print('For the BLACK spots, AVGsize=', avg_black, 'and Std.Dev=', std_black )
print('For the WHITE spots, AVGsize=', avg_white, 'and Std.Dev=', std_white )
print()
print('The number of horiz_lines is:',horiz_lines,'representing a length of',length_horiz_lines)
print('The number of vert_lines is:',vert_lines,'representing a length of',length_vert_lines)
print()
print('The total length of black spots is:',length_black_spots,', representing a',round(length_black_spots/tot_length*100,2),'%')
print('The total length of white spots is:',length_white_spots,', representing a',round(length_white_spots/tot_length*100,2),'%')


###VISUALIZATION of IMAGE and HISTOGRAMS###

#plt.imshow(img,cmap='gray')
im_RGB = Image.open(image_png).convert('RGB')
draw = ImageDraw.Draw(im_RGB)

for i in range(0,len(y_)):
        draw.line((0, y_[i],img.shape[1],y_[i]), fill=(255,0,0), width=2)
f = plt.figure(1)
plt.imshow(im_RGB)

for j in range(0,len(x_)):
        draw.line((x_[j],0,x_[j],img.shape[0]), fill=(0,255,0), width=2)
plt.title('original image + measuring grid')
plt.imshow(im_RGB)
f.show()
####HISTOGRAM BLACK
g = plt.figure(2)
# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(array_all_black, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.25)
if scale==1:
    plt.xlabel('Size in pixels')
else:
    plt.xlabel('Size in microns')
plt.ylabel('Frequency')
plt.title('histogram for BLACK spots')
plt.text(avg_black*3, avg_black*3, r'$\mu='+str(avg_black)+',\ \sigma='+str(std_black)+'$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(top=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
g.show()
####HISTOGRAM WHITE
h = plt.figure(3)
# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(array_all_white, bins='auto', color='#0504ab',alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.25)
if scale==1:
    plt.xlabel('Size in pixels')
else:
    plt.xlabel('Size in microns')
plt.ylabel('Frequency')
plt.title('histogram for WHITE spots')
plt.text(avg_white*3, avg_white*3, r'$\mu='+str(avg_white)+',\ \sigma='+str(std_white)+'$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(top=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
h.show()

###CSV EXPORT###


 

