# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:38:37 2023
@author: mhask

Basic
    includes basic motion
        move(theta,T)
        forward(T)
        left(T)
        right(T)
        up(T)
        down(T)
        
        where T = Percentage of Max Thrust
        where theta = Angle w.r.t. X axis
        X axis - Along the length of the AUV
        Y axis - Towards the T1 thruster = Left thruster

"""
### Libraries Imported

import numpy as np


### Functions
def move(theta, T = 0.6):

    K = 20.594
    Tnorm = K*T
    theta = theta*np.pi/180
    offset = 20*np.pi/180
    alpha = np.sqrt(1+np.tan(theta)**2)
    T1 = (K/2)*(1/(np.sin(offset)*alpha) + (np.tan(theta))/(Tnorm*np.cos(offset)*alpha))
    T2 = (K/2)*(1/(np.sin(offset)*alpha) - (np.tan(theta))/(Tnorm*np.cos(offset)*alpha))
    P1 = round(100*T1/K)
    P2 = round(100*T2/K)
    return P1, P2

def forward(T = 0.6):
    
    P1 = round(T*100)
    P2 = round(T*100)
    
    return P1,P2

def left(T = 0.6):
    
    P1 = 0
    P2 = round(T*100)
    
    return P1,P2

def right(T = 0.6):
    
    P1 = round(T*100)
    P2 = 0
    
    return P1,P2


 
"""
pitch x
yaw y
roll z

def setAngle(theta=0):
    
    S1 = 2000*((theta+135)/270)+500
    S2 = 2000*((theta+135)/270)+500
    return S1,S2


def up(theta=20):
    
    P1 = 2000*((theta+135)/270)+500
    P2 = 2000*((theta+135)/270)+500
    
    return P1.P2

def down(theta= ):
    """