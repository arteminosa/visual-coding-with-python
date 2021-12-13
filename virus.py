#import time
from turtle import *

speed(13)
color('fuchsia')
bgcolor('black')
#time.sleep(5)
b = 200
while b > 0:
    right(b)
    forward(b * 2)
    b = b - 1
#time.sleep(3)