# -*- coding: utf-8 -*-
"""
Created: Mon Dec 28 18:56:12 2020
Author: Stacie
Summary: Script used to get ticker names that have valid FB prophet data on file. 
"""

#Import Libraries
import os,sys,warnings,numpy as np
from FBprop_gen import FBprop_gen
from GetDates import GetDates as GD
from GetStockNames_Quick import GSN
import time

#Append Path
sys.path.append(r"C:\Users\Stacie\Desktop\Python_Projects\TickerLists")

#Clean Out Plot Directory
s1,e1,e2=GD() #FindIdealDate
dir1=os.getcwd()    

#Get Stock Names
GSN()
f=open(dir1+'\\TickerLists\\TickerListMain.txt','r')
lis1=f.read().split('\n')

#Get Length for Days Before
start_time=time.time()
tw_min,y_dif_max=0,20
ch_p_lis,y_lower,y_upper=[],0,0
tw_lis,lis1_pass,lis1_fail=['% Change'],['Stock Name'],['Stock Name']
y_lower_lis,y_upper_lis=['Lower Limit'],['Upper Limit']

#Hide Unneeded Warnings
warnings.filterwarnings('ignore')

#Test All Tickers in the List        
for c1 in range(0,len(lis1)):
    try:
        #Get Tw value and Difference in y values
        tw,y_dif=FBprop_gen(lis1[c1],1,s1,e1,tw_min,y_dif_max,1)

        #Case of Pass, Positive Tw So Save to Array
        if tw>tw_min and y_dif<y_dif_max:
            tw_lis.append(tw)
            lis1_pass.append(lis1[c1])
            print(str(c1)+": "+str(lis1[c1]))

        #Case of Fail for Negative 7 Week Value
        else:
            lis1_fail.append(lis1[c1])            
            print(str(c1)+": "+str(lis1[c1])+" - FAIL, FBPROP")

    #Case of Fail, Yfinance Can't Find Stock           
    except ValueError:
        print(str(c1)+": "+str(lis1[c1])+' - FAIL, YFINANCE')
        lis1_fail.append(lis1[c1])
        pass

#Save as Array in csv File for Ticker Lists that are Valid
arr1=np.asarray(lis1_pass)
np.savetxt('1_ImportStocks_Pass.csv',arr1,fmt='%s',delimiter='\t',encoding='utf-8')
