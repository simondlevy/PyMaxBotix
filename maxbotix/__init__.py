'''
Python classes for reading from MaxBotix ultrasonic ranging sensors.

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

import serial
import threading

class _MaxBotix(object):

    def __init__(self, port, baud):

        self._device = serial.Serial(port, baud)
        self._digits = ''
        self._running = False
        self._ready = False
        

    def _update(self, _ignore):

        while self._running:

            c = self._device.read(1)

            if c == 'R':

                self._ready = True
                self._digits = ''

            elif ord(c) == 13:    # carriage return

                if self._ready:
                    self.handleUpdate(int(self._digits))

                self._ready == False

            else:
                
                self._digits += c


    def start(self):
        '''
        Starts data acquisition on the sensor.
        '''
 
        self._ready = False
        self._digits = ''

        self._running = True

        t = threading.Thread(target=_MaxBotix._update, args = (self, None))
        t.daemon = True
        t.start()

    def stop(self):
        '''
        Stops data acquisition on the sensor.
        '''
 
        self._running =  False

        self._device.close()


class USB_ProxSonar(_MaxBotix):
    '''
    An abstract class for USB-ProxSonar-EZ sensors. Your subclass should implement the method 

        handleUpdate(self, distanceMillimeters) 
    '''

    def __init__(self, port):
        '''
        Opens a connector to a USB-ProSonar-EZ sensor on the specified port.
        '''

        _MaxBotix.__init__(self, port, 57600)

class XL_MaxSonar(_MaxBotix):
    '''
    An abstract class for XL-MaxSonar-EZ sensors.Your subclass should implement the method 

        handleUpdate(self, distanceCentimeters) 

    '''


    def __init__(self, port):
        '''
        Opens a connector to a XL-MaxSonar-EZ sensor on the specified port.
        '''

        _MaxBotix.__init__(self, port, 9600)
