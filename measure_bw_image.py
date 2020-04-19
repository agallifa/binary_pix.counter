# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:51:40 2020

@author: adria. 

The program counts the distance (in pixels) of black and white zones along 
10 vertical and 10 horizontal equispaced lines
"""
import numpy as np
import matplotlib.image as mpimg
from count_bw_array import count_bw_array

def measure_bw_image(image_png,x_lines,y_lines):
    #x equals vertical lines!
    #y equals horizontal lines!
    img = mpimg.imread(image_png)
    x_coord=np.linspace(0,img.shape[1], num=(x_lines+2))
    x_coord=np.around(x_coord[1:x_lines+1])
    x_=x_coord.astype(int)
    
    y_coord=np.linspace(0,img.shape[0], num=(y_lines+2))
    y_coord=np.around(y_coord[1:y_lines+1])
    y_=y_coord.astype(int)
    
    L_x_primer=[]
    L_x_all_b=[];L_x_all_w=[]
    L_x_avg_b=[];L_x_avg_w=[]
    L_x_std_b=[];L_x_std_w=[]
    
    L_y_primer=[]
    L_y_all_b=[];L_y_all_w=[]
    L_y_avg_b=[];L_y_avg_w=[]
    L_y_std_b=[];L_y_std_w=[]
        
    for i in range(0,len(x_)):
        vector_vert=img[0:-1,x_[i]]
        (first_color_x,M_b_x,av_b_x,std_b_x,M_w_x,av_w_x,std_w_x)=count_bw_array(vector_vert)
        L_x_primer.append(first_color_x)#1 if first in the line is white, 0 if black
        L_x_all_b.append(M_b_x)#gives a list with an array with sizes of black spots, per each line
        L_x_all_w.append(M_w_x)
        L_x_avg_b.append(av_b_x)#gives an array with the average of every line, individually
        L_x_avg_w.append(av_w_x)
        L_x_std_b.append(std_b_x)#gives an array with the std dev of every line, individually
        L_x_std_w.append(std_w_x)
    arr_x_b= np.hstack(L_x_all_b)#gives a flattened array containing the size of all the black spots, in all x lines
    arr_x_w= np.hstack(L_x_all_w)
        
    for j in range(0,len(y_)):
        vector_horiz=img[y_[j],0:-1]
        (first_color,M_b,av_b,std_b,M_w,av_w,std_w)=count_bw_array(vector_horiz)
        L_y_primer.append(first_color)
        L_y_all_b.append(M_b)
        L_y_all_w.append(M_w)
        L_y_avg_b.append(av_b)
        L_y_avg_w.append(av_w)
        L_y_std_b.append(std_b)
        L_y_std_w.append(std_w)
    arr_y_b= np.hstack(L_y_all_b)
    arr_y_w= np.hstack(L_y_all_w)
    
    return L_x_all_b, L_x_all_w, arr_x_b, arr_x_w, L_y_all_b, L_y_all_w, arr_y_b, arr_y_w, x_, y_
    #return L_x_primer, L_x_all_b, L_x_all_w, L_x_avg_b, L_x_avg_w,L_x_std_b, L_x_std_w, arr_x_b, arr_x_w, L_y_primer, L_y_all_b, L_y_all_w, L_y_avg_b, L_y_avg_w,L_y_std_b, L_y_std_w, arr_y_b, arr_y_w
    #to call function:
    #L_x_primer, L_x_all_b, L_x_all_w, L_x_avg_b, L_x_avg_w,L_x_std_b, L_x_std_w, arr_x_b, arr_x_w, L_y_primer, L_y_all_b, L_y_all_w, L_y_avg_b, L_y_avg_w,L_y_std_b, L_y_std_w, arr_y_b, arr_y_w = measure_bw_image('pattern3_bin.png',10,10)


            