"""
Name: Stacie
Date: Thu Jan 16 15:38:22 2020
About: Used to Generate an Excel File of Key Presses Until Keyboard Interrupt
"""

#Import Libraries
import win32api, pyautogui, csv

#Get State of Key
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

#Save File as Python Coordinate in Folder
file='Python_Coordinates'
c1,list1=0,[] #Declare Default Variables for Counter and List
list1.append(["Click #", "x","y", "Left or Right Click?"]) #Declare Headers for List

#Get State of Key
try:
    #Loop Counter to Get Key State
    while True:
	#Set Left and Right Keys to Default States
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
    
        if a != state_left:  # Left Button State Changed
            state_left = a #Reset State of Key
	    #If State is Less than 0 - Button Pressed
            if a < 0:
                c1=c1+1 #Add to Counter
                x, y = pyautogui.position() #Store X, Y Coordinates
                list1.append([str(c1),str(x),str(y),"Left"]) #Append to List
        if b != state_right:  # Right Button State Changed
            state_right = b #Reset State of Key
	    #If State is Less than 0 - Button Pressed
            if b < 0:
                c1=c1+1 #Add to Counter
                x, y = pyautogui.position() #Store X, Y Coordinates
                list1.append([str(c1),str(x),str(y),"Right"]) #Append to List

#If KeyboardInterrupt Keys Pressed, Save Lists to Excel
except KeyboardInterrupt:
    with open(file+'.csv', 'w+',newline='') as file:
        writer=csv.writer(file)
        for c2 in range(0,len(list1)):
            writer.writerow(list1[c2])
    
    print('\n\nDone.')

