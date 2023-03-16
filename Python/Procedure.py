"""
Created on Mon Mar 13 16:45:14 2023

@author: mhask

Procedure
    Calls the different libraries to run a specific procedure
    
"""

import Basic
import Comms
import ControlAUV
import time

ControlAUV.setup()

P1,P2 = Basic.forward()
Comms.pwm_to_thruster(P1, P2)
time.sleep(20)

P1,P2 = Basic.left()
Comms.pwm_to_thruster(P1,P2)
time.sleep(5)

P1,P2 = Basic.forward()
Comms.pwm_to_thruster(P1, P2)
time.sleep(20)
