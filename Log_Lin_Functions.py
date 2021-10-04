# -*- coding: utf-8 -*-
"""
Created: Fri Aug 14 16:17:56 2020
Author: Stacie
Summary: Functions used for logarithmic and linear fits to determine better mathematical models for approximations. 
"""

#Import Libraries
from GetPlot import GP
import numpy as np

#Function to Define Logarithmic Earnings 
def LogEarn(str3,str5,stock,c1,x,x_num,y_slog, y_slin,y,z_log):

    #Generate Plots and Save to Folder using the Functions
    GP(str5,stock[c1],np.append(x,x_num),y_slog,x,y,"_log")
    GP(str3,stock[c1],np.append(x,x_num),y_slin,x,y,"_lin")

    #Plot a Logarithmic Trend with Different Offsets
    p0=z_log[1]+z_log[0]*np.log(len(x))
    p1=z_log[1]+z_log[0]*np.log(len(x)+30.42)
    pp1=(p1-p0)/p0*100
    p6=z_log[1]+z_log[0]*np.log(len(x)+182.5)
    pp6=(p6-p0)/p0*100
    p12=z_log[1]+z_log[0]*np.log(len(x)+365)
    pp12=(p12-p0)/p0*100

    #Return Values Determined by Fits
    return p0,p1,pp1,p6,pp6,p12,pp12

#Function to Define Linear Earnings 
def LinEarn(str4,str3,str5,stock,c1,x,x_num, y_slog, y_slin,y,z_lin):

    #Generate Plots and Save to Folder using the Functions
    GP(str4,stock[c1],np.append(x,x_num),y_slin,x,y,"_lin")
    GP(str3,stock[c1],np.append(x,x_num),y_slog,x,y,"_log")

    #Plot a Linear Trend with Different Offsets
    p0=z_lin[1]+z_lin[0]*len(x)
    p1=z_lin[1]+z_lin[0]*(len(x)+30.42)
    pp1=(p1-p0)/p0*100
    p6=z_lin[1]+z_lin[0]*(len(x)+182.5)
    pp6=(p6-p0)/p0*100
    p12=z_lin[1]+z_lin[0]*(len(x)+365)  
    pp12=(p12-p0)/p0*100

    #Return Values Determined by Fits
    return p0,p1,pp1,p6,pp6,p12,pp12