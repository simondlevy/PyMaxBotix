maxbotix
========

maxbotix.py - Python classes for reading from MaxBotix ultrasonic ranging sensors

<p>

I needed an easy way to access data from the <a href="http://www.maxbotix.com/">MaxBotix</a> ultrasonic sensors using 
Python, so I wrote this little package, which you can 
<a href="https://github.com/simondlevy/PyMaxBotix">download from github</a>.  
It runs on Windows, Linux, and
OS X in Python 2 and 3.  As with the <a href="http://home.wlu.edu/~levys/software">other Python packages</a> I've 
written, the API is very simple.  For example, this program prints the distance in millimeters obtained from the
USB-ProxSonar-EZ sensor:

<b>
<pre>
from maxbotix import USB_ProxSonar

class MySensor(USB_ProxSonar):

    def __init__(self, port):
        USB_ProxSonar.__init__(self, port)

    def handleUpdate(self, distanceMillimeters):
        print('%d mm' % distanceMillimeters)

sensor = MySensor('COM8')

sensor.start()
</pre>
</b>

As this example shows, <tt><b>USB_ProxSonar</b></tt> is an abstract class that you subclass with a class implementing the
<tt><b>handleUpdate</b></tt> method.  The complete documentation is <a href="maxbotix.html">here</a>.


<h3>Instructions</h3>

You will need:

<ol>

<li> <p> The ability to program in Python
<p><li> The <a href="http://pyserial.sourceforge.net/">PySerial</a> package installed on your computer.  
Like many people, I found it easiest to <a href="http://pyserial.sourceforge.net/pyserial.html#from-source-tar-gz-or-checkout">install from source</a>.

<p><li>Administrator (root) privileges on your computer

<p><li>The PyMaxBotix <a href="https://github.com/simondlevy/PyMaxBotix">repository</a>.  

<p><li> A <a href="http://www.maxbotix.com/">MaxBotix</a> sensor.  As shown in the image above, I have both a 
<a href="http://www.maxbotix.com/Ultrasonic_Sensors/USB_Proximity_Sensor.htm">USB-ProxSonar-EZ</a> and a
<a href="http://www.maxbotix.com/Ultrasonic_Sensors/MB1240.htm">MB1240 XL-MaxSonar-EZ4</a> unit.  
I love the convenience of USB, but
Maxbotix <a href="http://www.maxbotix.com/SelectionGuide/indoor-uav.htm#uav">recommends</a>
 the MB1240 for Unmanned Aerial Vehicle (UAV) applications, which is my focus these days. To use this 
sensor on a USB port, I bought a 5-volt <a href="https://www.sparkfun.com/products/9718">FTDI adapter cable</a> and
reversed its RX polarity by following the instructions 
<a href="http://diydrones.com/profiles/blogs/frsky-s-cppm-at-27msec-firmware-update-with-ft-prog-and-ftdi-cabl">here</a>.
I soldered a seven-pin <a href="https://www.sparkfun.com/products/10158">header</a> onto the MB1240 for the +5v, GND, and RX (receive) lines, and
other signals, and used some 
<a href="https://www.sparkfun.com/products/12794">6" Male/Female jumper wires</a>
to connect the FTDI adapter to the headers.

</ol>

Once you've downloaded the repository, use a terminal (Linux or OS X) or command shell
(Windows) to change to the directory where you put it, and issue the command

<b>
<pre>
  python setup.py install
</pre>
</b>

On Linux or OS X, you may need to issue this command as root:

<b>
<pre>
  sudo python setup.py install
</pre>
</b>

Then you should be able to run the <b>usb_prox_sonar_test.py</b> or <b>xl_max_sonar_test.py</b> program,
depending on which sensor you have.   Be sure to determine the port to which the sensor is connected and
modify the test program accordingly.

<p>



<h3>Copyright and licensing</h3>

Copyright and licensing information (Gnu 
<a href="https://www.gnu.org/licenses/lgpl.html">LGPL</a>) 
can be found in the header of each source file.

