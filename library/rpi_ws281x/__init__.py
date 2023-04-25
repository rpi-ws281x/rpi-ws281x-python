# New canonical package, to support `import rpi_ws281x`
from .rpi_ws281x import PixelStrip, Adafruit_NeoPixel, Color, RGBW, ws
from _rpi_ws281x import *

__version__ = '5.0.0'
