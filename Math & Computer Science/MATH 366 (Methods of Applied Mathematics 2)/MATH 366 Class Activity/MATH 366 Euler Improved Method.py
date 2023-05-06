# -*- coding: utf-8 -*-
"""
This program implements improved Euler's (Heun's) Method for solving an ODE.
This is a predictor-corrector method. 
User input:
    x0 = initial x value
    y0 = initial y value
    h = step size
    N = number of iterations
"""

import numpy as np
import matplotlib.pyplot as plt

def yeimp(x):           #Exact solution to ODE
    return np.exp(x) - x - 1.0
    
def feimp(x,y):         #This is the formula for y' from ODE
    return y + x

def eulerimp(x0,y0,h,N):  #Improved Euler Method (Heun's Method)
    xn = np.zeros(N+1)          #Initialize x nodes
    yn = np.zeros(N+1)          #Initalize Improved Euler yn values
    xn[0] = x0
    yn[0] = y0
    for k in range(1,N+1):
        xn[k] = xn[k-1] + h             #Generate x nodes
        k1 = h*feimp(xn[k-1],yn[k-1])       #Predictor component
        k2 = h*feimp(xn[k],yn[k-1]+k1)      #Corrector component
        yn[k] = yn[k-1] + 0.5*(k1+k2)   #Generate Improved Euler yn values
    
    print('Improved Euler Solution=', yn)
                   
    #Next, we sample y on n=100 x values and plot f & y
    n = 100                              
    xvalues = np.zeros(n+1)    #Initialize x vector to be zeros
    yvalues = np.zeros(n+1)    #Initialize y vector to be zeros
    
    step = (xn[N]-x0)/n   #Use this step to get xinterval = [x0,xn(N)].   
    for k in range(0,n+1):
        xvalues[k] = x0 + k*step      #Generate vector of x values
        yvalues[k] = yeimp(xvalues[k])    #Generate vector of y(x) values
               
    plt.plot(xvalues,yvalues,'b',xn,yn,'o--k')   
    plt.xlabel('x')
    plt.legend(('Exact','Improved Euler'),loc = 0)
    plt.show()
    
         
        
    