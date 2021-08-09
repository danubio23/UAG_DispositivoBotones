import time
import os
import board
import digitalio
print("press a button!")

button1 = digitalio.DigitalInOut(board.D18)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

while True:
    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if not button1.value:
        os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_azul.m4a &')
        time.sleep(3)
        
    time.sleep(.25)
