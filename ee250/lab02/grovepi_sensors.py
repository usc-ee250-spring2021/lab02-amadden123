""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')
import grove_oled
import grovepi
import grove_128_64_oled as oled
import atexit

atexit.register(grovepi.encoder_dis)
grovepi.encoder_en()

grove_oled.oled_init()

grove_oled.oled_clearDisplay()
grove_oled.oled_setNormalDisplay()
oled.setPageMode()

ultrasonic_ranger = 4
potentiometer = 0
sensor_value = 0

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
	PORT = 4    # D4
	sensor_value = grovepi.analogRead(potentiometer)
	while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
		distance = ultrasonicRead(ultrasonic_ranger)
		
		grove_oled.oled_putString(sensor_value)
        
        #if sensor_value < distance:
		#	for i in range(0,9):
		#		grove_oled.oled_setText(i,0)
		#		grove_oled.oled_putString("OBJ PRESS")
		time.sleep(0.2)
		print(grovepi.ultrasonicRead(PORT))

	
