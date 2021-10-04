# -*- coding: utf-8 -*-
"""
Created: May 5 18:27:38 2020
Author: Stacie
Summary: Code used to count the frequency of words present in titles of CNN articles. The information of the words as well as their frequencies are saved in sheets within an Excel file. 
"""

#Get Libraries
import urllib, bs4, datetime, pandas as pd, xlrd
from urllib.request import Request
from RemoveTheseWords import RTW
from xlutils.copy import copy
import matplotlib.pyplot as plt

#Create Empty Lists and Strings
str_date=""
str_date1=[]
str_list=[]
word_freq=[]
x_save=[]
y_save=[]
[removal, replace_words]=RTW()

#Generate MATLAB Figure
plt.figure()
plt.figure(figsize=(10,7))

#Run Through Loop for Each Day
for d1 in range(1,5): #Range of Dates: This is From 1 to 5 Days Ago

    #Get Dates and Website Link
    word_freq=[]
    str5=datetime.datetime.now()-datetime.timedelta(days=d1)
    str_date=str5.strftime("%Y.%m.%d")
    str0='http://transcripts.cnn.com/TRANSCRIPTS/'+str_date+'.html'    
    str1=urllib.request.urlopen(Request(str0))
    webpage=str(str1.read())

    #Get HTML and XML from Webpage
    soup=bs4.BeautifulSoup(webpage,'lxml')
    links = soup.find_all('a', href=True)
        
    #Loop to Replace Similar Words
    for c2 in range(0,len(links)):
        str_name=links[c2].get_text()
        str_name=str_name.lower()       

        for c3 in range(0,len(replace_words),2):
            str_name=str_name.replace(replace_words[c3],replace_words[c3+1])

        str_list.append(str_name)

    #Split Up the Strings
    word_list="".join(str_list).split()
    
    #Replace Start if Matches "et"    
    for c2 in range(0,len(word_list)):
        if word_list[c2].startswith('et')==True:
            word_list[c2]=(word_list[c2])[2:]
    
    #Remove Unneeded Words From Previous Runs
    for c4 in removal:
        word_list=list(filter(lambda var: var != c4, word_list))
    
    #Count the Frequency of the Words
    for c3 in word_list:
        word_freq.append(word_list.count(c3))
    
    #Remove Words with Less than Five Occurances   
    remove_ind=[c5 for c5 in word_freq if c5 <= 5]
    ress = list(filter(lambda k: k <= 5, word_freq))
    
    #Put Into Array
    DF=pd.DataFrame({'Names':word_list,'Frequency':word_freq})
    
    #Sort By Frequency
    DF_sorted=DF.sort_values(by='Frequency',ascending=False)
    
    #Remove Duplicates
    DF_2=DF_sorted.drop_duplicates(subset='Names', keep="first", inplace=False)
  
    #Save to Excel File
    name1=str(d1)
    book_name=xlrd.open_workbook("Python_DailyNews.xlsm")
    book_name=copy(book_name)

    #Add Excel Sheet
    try:
        sheet1=book_name.add_sheet(str_date)
    except Exception:
        continue
    
    #Input the Name and Frequency
    str1=DF_2['Names']
    str1.sort_index(ascending=True)
    list1=list(str1.index)
    str2=DF_2['Frequency']
    str2.sort_index(ascending=True)
    list2=list(str2.index)
    
    #Write Data to Sheets
    for c2 in range(0,len(DF_2)):
        sheet1.write(1+c2,1+2*d1,str1[list1[c2]])
        sheet1.write(1+c2,2*d1,str(str2[list2[c2]]))
    book_name.save("Python_DailyNews.xlsm")
