# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:18:15 2023

@author: mhask

Comms
    includes communication with the thrusters and servos
        pwm_to_servo
        pwm_to_thruster

"""
from adafruit_servokit import ServoKit
import adafruit_pca9685

kit = ServoKit(channels=16)

def pwm_to_thruster(P1, P2):
    
    
    kit.servo[5].angle = P1
    kit.servo[4].angle = P2
    
def pwm_to_servo(Num, theta):
    
    # Kit commands
    if Num == 1:
        kit.servo[7].angle = 180-theta-13
    if Num == 2:
        kit.servo[6].angle = theta+3
        
    
    


