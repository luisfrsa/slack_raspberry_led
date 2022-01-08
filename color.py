from rpi_ws281x import *
import time

class Color:
    
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

    def __init__(self, ledStrip): 
        self.ledStrip = ledStrip.ledStrip
        self.ledStrip.begin()

    def red(self):
        self.writeAll(self.RED)
    
    def green(self):
        self.writeAll(self.GREEN)
    
    def blue(self):
        self.writeAll(self.BLUE)

    def writeAll(self, color):
        for x in range(0,LedStrip.LED_COUNT):
            self.ledStrip.setPixelColor(x,Color(color[0],color[1],color[2]))
        self.ledStrip.show()
        time.sleep(0.5)
    
    def gradient(self, color):
        for x in range(0,LedStrip.LED_COUNT):
            self.ledStrip.setPixelColor(x,Color(color[0],color[1],color[2]))
            self.ledStrip.show()
            time.sleep(0.008)


    def rainbow():
        for _ in range(100):
            color.writeAll(color.RED)
            color.writeAll(color.ORANGE)
            color.writeAll(color.YELLOW)
            color.writeAll(color.GREEN)
            color.writeAll(color.BLUE_GREEN)
            color.writeAll(color.BLUE)
            color.writeAll(color.PINK)

    def rgb():
        for _ in range(100): 
            color.gradient(color.RED)
            color.gradient(color.BLUE)
            color.gradient(color.GREEN)

    def seven_shifts():
        for _ in range(100):
            color.gradient(color.SEVEN_SHIFTS_ORANGE)
            color.gradient(color.SEVEN_SHIFTS_MINT)

    def red_orange():
        for _ in range(100):
            color.writeAll(color.RED)
            color.writeAll(color.ORANGE)
