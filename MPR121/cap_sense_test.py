#!/usr/bin/python
######################################################################
"""
cap_sense_test.py - demo to use 12-channel MPR121 capacitive touch
	sensor controller as a sound board.

Bart Spainhour <bart@tinkernauts.org>
	
From Freescale Semiconductor whitepaper:
 Proximity Capacitive Touch Sensor Controller - MPR121 OVERVIEW
 The MPR121 is the second generation capacitive touch sensor controller
 after the initial release of the MPR03x series devices. The MPR121
 features increased internal intelligence, some of the major additions
 include an increased electrode count, a hardware configurable I2C
 address, an expanded filtering system with debounce, and completely
 independent electrodes with auto-configuration built in. The device
 also features a 13th simulated sensing channel dedicated for near
 proximity detection using the multiplexed sensing inputs.
"""
######################################################################
import sys
import time
import Adafruit_MPR121.MPR121 as MPR121
import os

######################################################################
__author__ = "Bart Spainhour"
__email__ = "bart@tinkernauts.org"

######################################################################
# Open communication with MPR121 using default I2C address (0x5A)
# Create MPR121 instance
cap = MPR121.MPR121()

# Check for MPR121 initialization failure
if not cap.begin():
    print 'MPR121 init error; check connections.'
    sys.exit(1)

######################################################################
# Set sound samples for each cap sensor channel
#
# Drum Kit Layout
#
sound00 = "samples/drum_cymbal_hard.wav"
sound01 = "samples/drum_cymbal_closed.wav"
sound02 = "samples/drum_cymbal_open.wav"
sound03 = "samples/drum_tom_hi_hard.wav"
sound04 = "samples/drum_tom_mid_hard.wav"
sound05 = "samples/drum_tom_lo_hard.wav"
sound06 = "samples/drum_splash_hard.wav"
sound09 = "samples/drum_splash_soft.wav"
sound07 = "samples/drum_heavy_kick.wav"
sound08 = "samples/drum_snare_hard.wav"
sound10 = "samples/drum_bass_hard.wav"
sound11 = "samples/drum_bass_soft.wav"

# # Animal Noise Layout
# # 
# sound00 = "sounds/Animal/Horse.wav"
# sound01 = "sounds/Animal/Bird.wav"
# sound02 = "sounds/Animal/Crickets.wav"
# #
# sound03 = "sounds/Animal/Dog2.wav"
# sound04 = "sounds/Animal/Kitten.wav"
# sound05 = "sounds/Animal/Owl.wav"
# #
# sound06 = "sounds/Animal/Duck.wav"
# sound09 = "sounds/Animal/WolfHowl.wav"
# #
# sound07 = "sounds/Animal/Rooster.wav"
# sound08 = "sounds/Animal/Dog1.wav"
# #
# sound10 = "sounds/Animal/Goose.wav"
# sound11 = "sounds/Animal/Meow.wav"

# other sounds from Sonic Pi /opt/sonic-pi/etc/:
#	samples/drum_cymbal_pedal.wav
#	samples/drum_snare_soft.wav
#	samples/drum_tom_hi_soft.wav
#	samples/drum_tom_lo_soft.wav
#	samples/drum_tom_mid_soft.wav
#	samples/drum_cymbal_soft.wav	

# other sounds from Scratch /usr/share/scratch/Media/:
#	sounds/Animal/Horse.wav
#	sounds/Animal/HorseGallop.wav
#	sounds/Animal/Bird.wav
#	sounds/Animal/Crickets.wav
#	sounds/Animal/Dog2.wav
#	sounds/Animal/Kitten.wav
#	sounds/Animal/Meow.wav
#	sounds/Animal/Owl.wav
#	sounds/Animal/Duck.wav
#	sounds/Animal/WolfHowl.wav
#	sounds/Animal/Rooster.wav
#	sounds/Animal/Cricket.wav
#	sounds/Animal/Dog1.wav
#	sounds/Animal/Goose.wav
#	sounds/Animal/SeaLion.mp3
#	sounds/Animal/Cat.mp3

# Main Loop
try:
	print 'Press Ctrl-C to quit.'
	while True:
		if cap.is_touched(0):
			# print 'pin 00 touched'
			os.system('aplay -q ' + sound00 +' &')
			#
		if cap.is_touched(1):
			# print 'pin 01 touched'
			os.system('aplay -q ' + sound01 +' &')
		#
		if cap.is_touched(2):
			# print 'pin 02 touched'
			os.system('aplay -q ' + sound02 +' &')
		#	
		if cap.is_touched(3):
			# print 'pin 03 touched'
			os.system('aplay -q ' + sound03 +' &')
		#	
		if cap.is_touched(4):
			# print 'pin 04 touched'
			os.system('aplay -q ' + sound04 +' &')
		#
		if cap.is_touched(5):
			# print 'pin 05 touched'
			os.system('aplay -q ' + sound05 +' &')
		#
		if cap.is_touched(6):
			# print 'pin 06 touched'
			os.system('aplay -q ' + sound06 +' &')
		#
		if cap.is_touched(7):
			# print 'pin 07 touched'
			os.system('aplay -q ' + sound07 +' &')
		#
		if cap.is_touched(8):
			# print 'pin 08 touched'
			os.system('aplay -q ' + sound08 +' &')
		#
		if cap.is_touched(9):
			# print 'pin 09 touched'
			os.system('aplay -q ' + sound09 +' &')
		#
		if cap.is_touched(10):
			# print 'pin 10 touched'
			os.system('aplay -q ' + sound10 +' &')
		#
		if cap.is_touched(11):
			# print 'pin 11 touched'
			os.system('aplay -q ' + sound11 +' &')
		#
		# 
		time.sleep(0.1)

except KeyboardInterrupt:
        print ''
        print 'End.'
        sys.exit(1)
