#####INFORMATION
#Name: Stacie Herda
#Class: 213a Linear Algebra
#Quarter: Winter 2021
#Date Submitted: 1/27/2021
#Title: Hw#1 Prob#10

#####CODE
#####Prob10a

#Import Libraries
import matplotlib.pyplot as plt

#Get Array for Discrete Values for Function
#Go Up to 2081 Since Last Point is Removed and Want 2.080 as LastPoint
f_x=list(range(1920,2081,1)) 

# Divide by 1000 Since Range Only Takes Floats Instead of Integers
f_x=[num/1000 for num in f_x]

#Input Into Function
f_y=[(num-2)**9 for num in f_x]

#Create Graph for Parta
fig=plt.figure()
plt.plot(f_x,f_y,'b.')
plt.title('Evalution of f(x)')
plt.xlabel('x')
plt.ylabel('y')

#####Prob10b
#Generate Points for the Equation
g_x=f_x
g_y=[num**9-18*num**8+144*num**7-672*num**6+2016*num**5-4032*num**4+
     5376*num**3-4608*num**2+2304*num-512
     for num in g_x]

#Plot Function: g(x)
fig=plt.figure()
plt.plot(f_x,f_y,'b.',)
plt.title('Evalution of f(x) and g(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(g_x,g_y,'g.')

#Print Example of x=2.01
f_y=[(num-2)**9 for num in [2.02]]
g_y=[num**9-18*num**8+144*num**7-672*num**6+2016*num**5-4032*num**4+
     5376*num**3-4608*num**2+2304*num-512
     for num in [2.02]]

#Output Results for Functions
print('f(x)=',f_y)
print('g(x)=',g_y)
