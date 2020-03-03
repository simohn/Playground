import RPi.GPIO as GPIO
import time

import vlc

# url = 'http://mp3stream1.apasf.apa.at:8000'
url = 'http://mp3stream7.apasf.apa.at:8000'
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(url)
media.get_mrl()
player.set_media(media)

player.play()

# Variable Counter definieren
Counter = False

# SoC als Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)  

# Pin 24 vom SoC als Input deklarieren und Pull-Down Widerstand aktivieren
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  

# ISR
def Interrupt(channel):  
    # Zugriff auf globale Variablen
    global Counter
    
    if Counter:
        player.play()
        print("Start Player")
        Counter = False
        
    else:
        player.pause()
        print("Stop Player")
        Counter = True
     
    
# Interrupt Event hinzufuegen. Pin 24, auf steigende Flanke reagieren und ISR "Interrupt" deklarieren
GPIO.add_event_detect(24, GPIO.RISING, callback = Interrupt, bouncetime = 500)   
  
# Endlosschleife
while True:
    time.sleep(10)

