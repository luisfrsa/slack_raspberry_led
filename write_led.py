from rpi_ws281x import *
from led import LedStrip
import time
from colour import Color as ColorRGB

class WriteLed:
    
    RED = [255,0,0]
    # ORANGE = [255,173,0]
    ORANGE = [255,15,0] # had to hack the green intensity to get an acceptable orange
    YELLOW = [255,250,0]
    GREEN = [50,255,0]
    BLUE_GREEN = [0,255,254]
    BLUE = [0,33,255]
    PINK = [255,0,191]
    SEVEN_SHIFTS_ORANGE = [255,0,50]
    SEVEN_SHIFTS_MINT = [58,189,169]
    BLACK = [0,0,0]

    def __init__(self, ledStrip): 
        self.ledStrip = ledStrip.ledStrip
        self.ledStrip.begin()

    def off(self):
        self.writeAll(self.BLACK)

    def red(self):
        self.writeAll(self.RED)
    
    def green(self):
        self.writeAll(self.GREEN)
    
    def blue(self):
        self.writeAll(self.BLUE)

    def writeAll(self, color, delay=0.5):
        for x in range(0,LedStrip.LED_COUNT):
            self.ledStrip.setPixelColor(x,Color(color[0],color[1],color[2]))
        self.ledStrip.show()
        time.sleep(delay)
    
    def gradient(self, color):
        for x in range(0,LedStrip.LED_COUNT):
            self.ledStrip.setPixelColor(x,Color(color[0],color[1],color[2]))
            self.ledStrip.show()
            time.sleep(0.008)

    def gradient2(self, colorFrom, colorTo, seconds=5):
        changeSpeed = 0.05
        numberOfColors = int(seconds/changeSpeed)
        colorInstance = ColorRGB(rgb=(self.rgbToColour(colorFrom[0]),self.rgbToColour(colorFrom[1]),self.rgbToColour(colorFrom[2])))
        print(colorInstance)
        colors = list(colorInstance.range_to(ColorRGB(rgb=(self.rgbToColour(colorTo[0]),self.rgbToColour(colorTo[1]),self.rgbToColour(colorTo[2]))),numberOfColors))
        for color in colors:
            newColor = [self.colourToRgb(color.rgb[0]),self.colourToRgb(color.rgb[1]),self.colourToRgb(color.rgb[2])]
            self.writeAll(newColor,changeSpeed)

    def rgbToColour(self,number):
        return number/255

    def colourToRgb(self,number):
        return int(number * 255) 

    def rainbow():
        for _ in range(100):
            write_led.writeAll(write_led.RED)
            write_led.writeAll(write_led.ORANGE)
            write_led.writeAll(write_led.YELLOW)
            write_led.writeAll(write_led.GREEN)
            write_led.writeAll(write_led.BLUE_GREEN)
            write_led.writeAll(write_led.BLUE)
            write_led.writeAll(write_led.PINK)

    def rgb():
        for _ in range(100): 
            write_led.gradient(write_led.RED)
            write_led.gradient(write_led.BLUE)
            write_led.gradient(write_led.GREEN)

    def seven_shifts():
        for _ in range(100):
            write_led.gradient(write_led.SEVEN_SHIFTS_ORANGE)
            write_led.gradient(write_led.SEVEN_SHIFTS_MINT)

    def red_orange():
        for _ in range(100):
            write_led.writeAll(write_led.RED)
            write_led.writeAll(write_led.ORANGE)
