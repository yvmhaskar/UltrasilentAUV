# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:29:02 2023

@author: mhask

 LEFT side == 1
 RIGHT side== 2
ControlAUV

"""
import Basic
import Comms
import time
import adafruit_bno055
from adafruit_servokit import ServoKit
from adafruit_extended_bus import ExtendedI2C as I2C

sensor = adafruit_bno055.BNO055_I2C(I2C(4))
kit = ServoKit(channels=16)

def setup():
    
    kit.servo[4].actuation_range = 100
    kit.servo[4].set_pulse_width_range(500, 2500)
    
    kit.servo[5].actuation_range = 100
    kit.servo[5].set_pulse_width_range(500, 2500)
    
    kit.servo[6].actuation_range = 180
    kit.servo[6].set_pulse_width_range(500, 2500)
    kit.servo[6].angle = 87
    
    kit.servo[7].actuation_range = 180
    kit.servo[7].set_pulse_width_range(500, 2500)
    kit.servo[7].angle = 103

def neutralAngle():
    
    kit.servo[7].angle = 87
    kit.servo[6].angle = 103
    
def followCam(y,z):

    if y < 0:
        P1,P2 = Basic.left()
    if y > 0:
        P1,P2 = Basic.right()
    else:
        P1 = 0
        P2 = 0
    
    Comms.pwm_to_thruster(P1, P2)
    
    
    theta = 60*(z+240)/480 + 60
    Comms.pwm_to_servo(1, theta)
    Comms.pwm_to_servo(2, theta)
    time.sleep(5)

def Autolevel():
    [yaw,pitch,roll] = sensor.euler
    if yaw > 45:
        [yaw,b,c] = sensor.quaternion
    if pitch > 45:
        [a,pitch,c] = sensor.quaternion
    if roll > 45:
        [a,b,roll] = sensor.quaternion
    p = 0
    q = 0
        
    while abs(pitch) > 20 or p >= 1000:
        theta = pitch/3 + 90
        Comms.pwm_to_servo(1, theta)
        Comms.pwm_to_servo(2, theta)
        P1,P2 = Basic.forward(0.3)
        Comms.pwm_to_thruster(P1, P2)
        p += 1
    Comms.pwm_to_thruster(0,0)
    while abs(roll) > 20 or q >=1000:
        ltheta = 90 - roll/3
        rtheta = 90 + roll/3
        Comms.pwm_to_servo(1, ltheta)
        Comms.pwm_to_servo(2, rtheta)
        Comms.pwm_to_thruster(P1, P2)
        time.sleep(5)
        Comms.pwm_to_thruster(0, 0)
        q += 1
            
    p = 0
    while abs(pitch) > 20 or p >= 1000:
        theta = pitch/3 + 90
        Comms.pwm_to_servo(1, theta)
        Comms.pwm_to_servo(2, theta)
        Basic.forward()
        Comms.pwm_to_thruster(P1, P2)
        time.sleep(5)
        Comms.pwm_to_thruster(0, 0)
        p += 1

def surface():
    
    theta = 120
    Comms.pwm_to_servo(1, theta)
    Comms.pwm_to_servo(2, theta)
    
    
    
    
    
    
    