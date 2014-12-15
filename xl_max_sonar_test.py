#!/usr/bin/env python
'''
xl_max_sonar_test.py - Test program for maxbotix.XL_Max_Sonar class

Copyright (C) 2014 Simon D. Levy


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
'''


PORT = '/dev/ttyUSB1' 	                  # Linux
#PORT = '/dev/tty.usbserial-A7Y5QR09'	  # Mac OS X (Darwin)
#PORT =  'COM8'                           # Windows

RUNTIME_SECONDS = 5

from maxbotix import XL_MaxSonar
from time import sleep

class MySensor(XL_MaxSonar):

    def __init__(self, port):

        XL_MaxSonar.__init__(self, port)

    def handleUpdate(self, distanceCentimeters):

        print('%d cm' % distanceCentimeters)

sensor = MySensor(PORT)

sensor.start()

sleep(RUNTIME_SECONDS)

sensor.stop()
