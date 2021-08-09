import time
import os
import board
import digitalio
print("press a button!")

button1 = digitalio.DigitalInOut(board.D18)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D23)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D24)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.D25)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.D12)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.D16)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

button7 = digitalio.DigitalInOut(board.D20)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.UP

#R: 1.11
button8 = digitalio.DigitalInOut(board.D21)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.UP

mode = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0
video = 0

# R: 1.1
while True:
    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if not button1.value:
        #R: 1.4
        #R: 1.4.1
        if mode == 0:
            if flag1 == 0:
                #R: 1.2
                #R: 1.3
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_azul.m4a &')
                flag1 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_azul_cielo.m4a &')
                flag1 = 0
        #R: 1.4.2
        else:
            if flag1 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_tigre.m4a &')
                flag1 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_vaca.m4a &')
                flag1 = 0
        time.sleep(3)

    if not button2.value:
        if mode == 0:
            if flag2 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_amarillo.m4a &')
                flag2 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_naranja.m4a &')
                flag2 = 0
        else:
            if flag2 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_caballo.m4a &')
                flag2 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_cerdo.m4a &')
                flag2 = 0
        time.sleep(3)

    if not button3.value:
        if mode == 0:
            if flag3 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_verde.m4a &')
                flag3 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_violeta.m4a &')
                flag3 = 0
        else:
            if flag3 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_chango.m4a &')
                flag3 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_elefante.m4a &')
                flag3 = 0
        time.sleep(3)
        
    if not button4.value:
        if mode == 0:
            if flag4 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_rojo.m4a &')
                flag4 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_cafe.m4a &')
                flag4 = 0
        else:
            if flag4 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_gallo.m4a &')
                flag4 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_gato.m4a &')
                flag4 = 0
        time.sleep(3)

    if not button5.value:
        if mode == 0:
            os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_apaga.m4a &')
        else:
            if flag5 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_leon.m4a &')
                flag5 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_pato.m4a &')
                flag5 = 0
        time.sleep(3)

    if not button6.value:
        if mode == 0:
            if flag6 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_blanca.m4a &')
                flag6 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/colores/color_rosa.m4a &')
                flag6 = 0
        else:
            if flag6 == 0:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_perro.m4a &')
                flag6 = 1
            else:
                os.system('omxplayer ../home/pi/Documents/audiobuttons/animales/animal_rana.m4a &')
                flag6 = 0
        time.sleep(3)
        
    if not button7.value:
        #R: 1.4
        #R: 1.4.3
        if video == 0:
            os.system('omxplayer ../home/pi/Documents/audiobuttons/videos/video_granjazenon.m4a &')
            video = 1
        elif video == 1:
            os.system('omxplayer ../home/pi/Documents/audiobuttons/videos/video_31minutos.m4a &')
            video = 2
        elif video == 2:
            os.system('omxplayer ../home/pi/Documents/audiobuttons/videos/video_elmo.m4a &')
            video = 3
        elif video == 3:
            os.system('omxplayer ../home/pi/Documents/audiobuttons/videos/video_lulukids.m4a &')
            video = 4
        elif video == 4:
            os.system('omxplayer ../home/pi/Documents/audiobuttons/videos/video_plimplim.m4a &')
            video = 0
        time.sleep(3)

    if not button8.value:
        if mode == 0:
            mode = 1
        else:
            mode = 0
        os.system('omxplayer ../home/pi/Documents/audiobuttons/controles/control_next.m4a &')
        time.sleep(3)
        
    time.sleep(.25)
