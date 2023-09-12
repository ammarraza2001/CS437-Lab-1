# Develop a program that enables the movement of a solitary pixel
# (represented by a single LED) within the SenseHat matrix. Control this pixel's movement using the
# Joystick interface. For example, assume the initial (x,y) coordinates of the pixel to be illuminated is set as
# (3,5). When the joystick is pushed in the right direction, the subsequent pixel along the positive X-axis
# should light up. Likewise, pressing the joystick upwards, downwards, or to the left should illuminate the
# respective corresponding pixel. Exit the program in case of the middle-click

from sense_hat import SenseHat
from time import sleep
import sys
sense = SenseHat()
sense.clear()
red = (255,0,0)

x,y = 0,2
sense.set_pixel(x, y, red)

#directions = {(0,1), (0,-1), (1,0), (-1,0)}
while True:
    
    for event in sense.stick.get_events():
        #print(event.direction,event.action)
        if event.action =="pressed" or event.action == "held": ## check if the joystick was pressed
            if event.direction=="middle":
                
                sys.exit(0)
            if event.direction=="down": ## to check for other directions use
                if(y + 1 <= 7):
                    y = y+1
            if event.direction=="up": ## to check for other directions use
                if(y -1 >= 0):
                    y = y-1
            if event.direction=="right": ## to check for other directions use
                if(x + 1 <= 7):
                    x = x+1
            if event.direction=="left": ## to check for other directions use
                if(x - 1 >= 0):
                    x = x - 1
            sense.clear()
            sense.set_pixel(x,y,red)
                    
                
            # "up", "down", "left", "right"
                
            #sleep(2) # # wait a while and then clear the screen
            #sense.clear()
