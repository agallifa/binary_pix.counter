# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:31:17 2020

@author: adria
"""
import numpy as np
#a=np.array([0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1]) 
def count_bw_array(a):
    #a=np.array([1,1,1,0,0,0,0,1,1,1,0,0,1,0,1])  
    #a=np.array([0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1]) 
    M=np.zeros(len(a))
    count=1
    index=0
    M[0,]=1 
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            count+=1
        else:
            index+=1
            count=1
        M[index,]=count
    M_final=M[M != 0]
    
    if a[0]==0:
        first_color=0
        mask_b= np.empty((len(M_final),))
        mask_b[::2] = 1
        mask_b[1::2] = 0
        
        mask_w= np.empty((len(M_final),))
        mask_w[::2] = 0
        mask_w[1::2] = 1
    else:
        first_color=1
        mask_w= np.empty((len(M_final),))
        mask_w[::2] = 1
        mask_w[1::2] = 0
        
        mask_b= np.empty((len(M_final),))
        mask_b[::2] = 0
        mask_b[1::2] = 1
    
    M_b=M_final*mask_b
    M_b=M_b[M_b != 0]
    M_w=M_final*mask_w
    M_w=M_w[M_w != 0]
    
    av_b=np.mean(M_b)
    av_w=np.mean(M_w)
    std_b=np.std(M_b)
    std_w=np.std(M_w)
    #print(a)
    #print(M_final)
    #print(first_color)
    #print(M_b)
    #print(M_w)
    return(first_color,M_b,av_b,std_b,M_w,av_w,std_w)