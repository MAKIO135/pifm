#!/usr/bin/python

import subprocess, signal, time
import RPi.GPIO as GPIO

station = 96.1

def play_sound( filename, channel=103.3 ):
    subprocess.Popen( [ "./pifm", filename, str(channel) ] )
    return

def reboot():
    print "goingToReboot"
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen( command.split(), stdout=subprocess.PIPE )
    output = process.communicate()[ 0 ]
    print output

GPIO.setmode( GPIO.BCM )

btn_pin = 14
btn_val = 0
GPIO.setup( btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

while True:
    tmp_val = GPIO.input( btn_pin )
    #print( tmp_val, btn_val )

    if tmp_val == 1 and btn_val == 0:
        play_sound( "sounds/star-wars.wav", station )
        time.sleep( 1 )

    elif tmp_val == 0 and btn_val == 1:
        GPIO.cleanup()
        reboot()

    btn_val = tmp_val
