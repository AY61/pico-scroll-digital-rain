from microbit import *
import random

brightness = [9, 6, 4] #Lead pixel, 1st trail then 2nd trail brightness
cols = [random.randint(0, 13) for _ in range(5)] #Make list of 5 random numbers for setting positions

while True:
    
    display.clear()
    
    for i in range(len(cols)):
        if cols[i] >= 10 and random.randint(0, 2) == 2: #Reset position with Random offset
            cols[i] = 0
        if cols[i] <= 4: #Lead pixel
            display.set_pixel(i, cols[i], brightness[0])
        if cols[i] <= 5 and cols[i] >= 1: #Trail pixel 1
            display.set_pixel(i, cols[i]-1, brightness[1])
        if cols[i] <= 6 and cols[i] >= 2: #Trail pixel 2
            display.set_pixel(i, cols[i]-2, brightness[2])
        cols[i] += 1 #Move everything along 1 for next pass through
    
    sleep(100)
