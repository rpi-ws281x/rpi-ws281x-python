# A short utility to set color and switch on/off the led strp

import sys, getopt
from rpi_ws281x import Color, PixelStrip, ws

# LED strip configuration:
LED_COUNT = 80        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STRIP = ws.SK6812W_STRIP


# Store RGBW values - Sanitize data when setting a color
class RGBW:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.white=0

    def setvalue(self, color, value):
        try:
            value = int(value)
        except:
            print (value, 'is not a valid value')
            Usage()
        match color:
            case "red":
                self.red = 0 if value < 0 else 255 if value > 255 else value
            case "green":
                self.green = 0 if value < 0 else 255 if value > 255 else value
            case "blue":
                self.blue = 0 if value < 0 else 255 if value > 255 else value
            case "white":
                self.white = 0 if value < 0 else 255 if value > 255 else value

# Display Help
def Usage():
    print ('usage:',sys.argv[0],'[options values] ...')
    print ('Options:')
    print ('r <value>    : set red intensity from 0 to 255')
    print ('g <value>    : set green intensity from 0 to 255')
    print ('b <value>    : set blue intensity from 0 to 255')
    print ('w <value>    : set white intensity from 0 to 255')
    print ('--off        : switch off the leds - rgb parameters ignored - equivalent to switchleds.py -r 0 -g 0 -b 0 -w 0')
    print ('Values lower than 0 or higher than 255 are respectively set to 0 or 255')
    quit()

# Main Logic
if __name__ == '__main__':

    #VARs
    # Create PixelStrip object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # RGBW Values
    rgbw = RGBW()
    off = False

    # Parse arguments
    try:
        options, remainer = getopt.getopt(sys.argv[1:], 'hr:g:b:w:', ['help', 'red=', 'green=', 'blue=', 'white=', 'off'])
    except getopt.GetoptError as err:
        print(err)
        Usage()

    # Check arguments and store RGBW values
    for opt, arg in options:
        if opt in ('-h', '--help'):
            Usage()
        elif opt in ('-r', '--red'):
            rgbw.setvalue('red', arg)
        elif opt in ('-g', '--green'):
            rgbw.setvalue('green', arg)
        elif opt in ('-b', '--blue'):
            rgbw.setvalue('blue', arg)
        elif opt in ('-w', '--white'):
            rgbw.setvalue('white', arg)
        elif opt == '--off':
            off = True

    # Useless argument warning
    if len(remainer) > 0:
        print (remainer, ': additional parameters ignored - type switchleds.py -h to get help')

    # Intialize the library (must be called once before other functions).
    strip.begin()
    color = Color(0,0,0,0) if off else Color(rgbw.red, rgbw.green, rgbw.blue, rgbw.white)
    for i in range(strip.numPixels()):
        # Set the color to every led
        strip.setPixelColor(i, color)
        strip.show()
