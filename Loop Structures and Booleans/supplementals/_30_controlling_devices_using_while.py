"""
Demonstrate controlling devices using while.
This Python program controls the animated star on the top of Kevin's Christmas tree.
The LED device used is:  https://www.adafruit.com/product/4222
The microcontroller that runs the Python program is: https://www.adafruit.com/product/3382
This program is written in a Python subset called CircuitPython: https://circuitpython.org
"""


import time
import board
import neopixel
import random
import my_time

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
NUMPIXELS = 44
INNER = (40, 43)
MIDDLE = (24, 39)
OUTER = (0, 23)
ENTIRE = (0, 43)
MIDDLE_AND_OUTER = (0, 39)

EW = (18, 36, 28, 6)
NS = (12, 32, 24, 0)
SWNE = (21, 38, 30, 9)
SENW = (3, 26, 34, 15)


def main():
    neopixels = neopixel.NeoPixel(board.D6, NUMPIXELS, brightness=0.2, auto_write=False)

    while True:
        animate_star_swirly(neopixels, 120)
        animate_star_twinkly(neopixels, 120);
        animate_star_inflate_deflate(neopixels, 120);
        animate_star_twirly(neopixels, 120);


def animate_star_swirly(star_pixels, limit_in_seconds):
    feature_timer = my_time.ElapsedTimer()
    while feature_timer.calculate_elapsed_seconds_as_int() < limit_in_seconds:
        set_pixels_from_range(star_pixels, OFF, ENTIRE)
        for i in range(43, -1, -1):
            star_pixels[i] = WHITE
            star_pixels.show()
            time.sleep(.005)
        time.sleep(3)
        for i in range (0, 44):
            star_pixels[i] = OFF
            star_pixels.show()
            time.sleep(.005)
        time.sleep(3)


def animate_star_twinkly(star_pixels, limit_in_seconds):
    feature_timer = my_time.ElapsedTimer()
    while feature_timer.calculate_elapsed_seconds_as_int() < limit_in_seconds:
        set_pixels_from_range(star_pixels, OFF, ENTIRE)
        star_pixels.show()
        set_pixels_from_range(star_pixels, WHITE, INNER)
        cycle_timer = my_time.ElapsedTimer()
        while cycle_timer.calculate_elapsed_seconds_as_int() < 4:
            set_pixels_randomly_from_range(star_pixels, MIDDLE_AND_OUTER)
            star_pixels.show()
            time.sleep(.0001)
        set_pixels_from_range(star_pixels, OFF, ENTIRE)
        star_pixels.show()
        time.sleep(3)


def set_pixels_randomly_from_range(the_pixels, pixel_range):
    start, stop = pixel_range
    for i in range(start, stop + 1):
        random_value = random.randint(0, 1)
        if random_value == 0:
            color = OFF
        else:
            color = WHITE
        the_pixels[i] = color


def animate_star_inflate_deflate(star_pixels, limit_in_seconds):
    feature_timer = my_time.ElapsedTimer()
    while feature_timer.calculate_elapsed_seconds_as_int() < limit_in_seconds:
        set_pixels_from_range(star_pixels, OFF, ENTIRE)
        star_pixels.show()
        time.sleep(.04)
        set_pixels_from_range(star_pixels, WHITE, INNER)
        star_pixels.show()
        time.sleep(.04)
        set_pixels_from_range(star_pixels, WHITE, MIDDLE)
        star_pixels.show()
        time.sleep(.04)
        set_pixels_from_range(star_pixels, WHITE, OUTER)
        star_pixels.show()
        time.sleep(3)
        set_pixels_from_range(star_pixels, OFF, OUTER)
        star_pixels.show()
        time.sleep(.04)
        set_pixels_from_range(star_pixels, OFF, MIDDLE)
        star_pixels.show()
        time.sleep(.04)
        set_pixels_from_range(star_pixels, OFF, INNER)
        star_pixels.show()
        time.sleep(3)


def set_pixels_from_range(the_pixels, color, pixel_range):
    start, stop = pixel_range
    for i in range(start, stop + 1):
        the_pixels[i] = color


def animate_star_twirly(star_pixels, limit_in_seconds):
    feature_timer = my_time.ElapsedTimer()
    while feature_timer.calculate_elapsed_seconds_as_int() < limit_in_seconds:
        set_pixels_from_range(star_pixels, OFF, ENTIRE)
        star_pixels.show()
        time.sleep(.04)
        set_pixels_from_range(star_pixels, WHITE, INNER)
        star_pixels.show()
        time.sleep(.04)
        cycle_timer = my_time.ElapsedTimer()
        while cycle_timer.calculate_elapsed_seconds_as_int() < 4:
            set_pixels_from_sequence(star_pixels, OFF, SWNE)
            set_pixels_from_sequence(star_pixels, OFF, SENW)
            set_pixels_from_sequence(star_pixels, WHITE, EW)
            set_pixels_from_sequence(star_pixels, WHITE, NS)
            star_pixels.show()
            time.sleep(.075)
            set_pixels_from_sequence(star_pixels, OFF, EW)
            set_pixels_from_sequence(star_pixels, OFF, NS)
            set_pixels_from_sequence(star_pixels, WHITE, SWNE)
            set_pixels_from_sequence(star_pixels, WHITE, SENW)
            star_pixels.show()
            time.sleep(.075)
        set_pixels_from_sequence(star_pixels, OFF, SWNE)
        set_pixels_from_sequence(star_pixels, OFF, SENW)
        set_pixels_from_range(star_pixels, OFF, INNER)
        star_pixels.show()
        time.sleep(3)


def set_pixels_from_sequence(the_pixels, color, pixel_sequence):
    for i in pixel_sequence:
        the_pixels[i] = color


main()
