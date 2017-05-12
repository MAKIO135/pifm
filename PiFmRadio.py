#!/usr/bin/python

import os, subprocess, signal, time
import RPi.GPIO as GPIO

station = 96.1

def play_sound( filename, channel=103.3 ):
    subprocess.Popen( [ "./pifm", filename, str(channel) ] )
    return

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
        # kill pifm process
        p = subprocess.Popen( [ 'ps', '-A' ], stdout=subprocess.PIPE )
        out, err = p.communicate()

        for line in out.splitlines():
            if 'pifm' in line:
                # print line
                pid = int( line.split( None, 1 )[ 0 ] )
                os.kill( pid, signal.SIGKILL )

        # clear GPIO4
        os.system( "echo  4 > /sys/class/gpio/export" )
        os.system( "echo  4 > /sys/class/gpio/unexport" )

    btn_val = tmp_val
