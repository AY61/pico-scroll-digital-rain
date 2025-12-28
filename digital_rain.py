from picoscroll import PicoScroll
import utime, random

sh = PicoScroll()
brightness = [120, 33, 10] #Lead pixel, 1st trail then 2nd trail brightness
cols = [random.randint(0, 15) for _ in range(17)] #Make list of 17 random numbers for setting positions

while True:
    sh.clear()
    for i in range(len(cols)):
        if cols[i] >= 15 and random.randint(0, 2) == 2: #Reset position with Random offset
            cols[i] = 0
        if cols[i] <= 6: #Lead pixel
            sh.set_pixel(i, cols[i], brightness[0])
        if cols[i] <= 7 and cols[i] >= 1: #Trail pixel 1
            sh.set_pixel(i, cols[i]-1, brightness[1])
        if cols[i] <= 8 and cols[i] >= 2: #Trail pixel 2
            sh.set_pixel(i, cols[i]-2, brightness[2])
        cols[i] += 1 #Move everything along 1 for next pass through
    if sh.is_pressed(sh.BUTTON_B): #Credits
        sh.scroll_text("Digital Rain by AY61", brightness[0], 30)
    sh.show()
    utime.sleep(0.1) #Delay