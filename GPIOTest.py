import RPi.GPIO as GP
import sys
from time import sleep
from types import *

#Set the layout of Pins
GP.setmode(GP.BCM)
#Set pins
GP.setup(23,GP.OUT,initial =0)
switch  = False;

for i in range(0,20):
    GP.output(23,switch)
    switch  = ~switch
    sleep(1)
#Reset Pin Settings
GP.cleanup()
sys.exit(0)
