#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

if os.path.exists(libdir):
  sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
from gpiozero import Button
from signal import pause
import traceback

# Constants
logging.basicConfig(level=logging.DEBUG)
# Display resolution
EPD_WIDTH       = 176
EPD_HEIGHT      = 264

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)
# GPIO.input(5)
# GPIO.input(6)
# GPIO.input(13)
# GPIO.input(19)

font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
font14 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)

blackimage = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)  # 255: clear the frame
redimage = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)  # 255: clear the frame

# Text
x = 25
y = 65
size = 14
fill = 0
font = font14

def init_epd():
  # epd = epd2in7.EPD() # B/W only
  epd = epd2in7b.EPD() # B/W/R
  logging.info("init and Clear")
  epd.init()
  epd.Clear()
  return epd

def display_image(epd, black_image, red_image):
  epd.display(epd.getbuffer(black_image), epd.getbuffer(red_image))
  # epd.sleep()

def display_text(epd, string, is_red, blank_image, x, y, size, fill, font):
  image = blank_image
  draw = ImageDraw.Draw(image)
  draw.text((x, y), string, font = font, fill = 0)

  if (is_red == True):
    epd.display(epd.getbuffer(blank_image), epd.getbuffer(image))
  else:
    epd.display(epd.getbuffer(image), epd.getbuffer(blank_image))

# def process_button(epd, pin):
#   # pin = btn.pin.number
#   # epd = init_epd()
#   print("button pressed")
#   print(pin)

#   blank_image = Image.new('1', (epd.width, epd.height), 255)

#   # 5, 6, 13, 19
#   if (pin == 5):
#     black_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
#     display_image(epd, black_image, blank_image)
#   if (pin == 6):
#     red_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
#     display_image(epd, blank_image, red_image)
#   if (pin == 13):
#     string = "The quick brown fox jumps over the lazy dog"
#     is_red = False

#     x = 25
#     y = 65
#     size = 14
#     fill = 0
#     font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)

#     display_text(epd, string, is_red, blank_image, x, y, size, fill, font)
#   if (pin == 19):
#     string = "The quick brown fox jumps over the lazy dog"
#     is_red = True

#     x = 25
#     y = 65
#     size = 14
#     fill = 0
#     font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)

#     display_text(epd, string, is_red, blank_image, x, y, size, fill, font)

  # epd.sleep()
  # epd2in7b.epdconfig.module_exit()
  # exit()

def snoopy(epd, pin):
  print("button pressed")
  epd.Clear()
  blank_image = Image.new('1', (epd.width, epd.height), 255)
  black_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
  display_image(epd, black_image, blank_image)

def snoopy_red(epd, pin):
  print("button pressed")
  epd.Clear()
  blank_image = Image.new('1', (epd.width, epd.height), 255)
  red_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
  display_image(epd, blank_image, red_image)

def error(epd, pin):
  print("button pressed")
  epd.Clear()

  black_image = Image.open(os.path.join(picdir, 'error2in7.bmp'))
  red_image = Image.open(os.path.join(picdir, 'error2in7_red.bmp'))
  display_image(epd, black_image, red_image)

def text_black(epd, pin):
  print("button pressed")
  epd.Clear()
  string = "The quick brown fox jumps over the lazy dog"
  is_red = False

  x = 25
  y = 65
  size = 14
  fill = 0
  font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)

  display_text(epd, string, is_red, blank_image, x, y, size, fill, font)

def text_red(epd, pin):
  print("button pressed")
  epd.Clear()
  string = "The quick brown fox jumps over the lazy dog"
  is_red = True

  x = 25
  y = 65
  size = 14
  fill = 0
  font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)

  display_text(epd, string, is_red, blank_image, x, y, size, fill, font)

epd = init_epd()
# horizontal (epd.height, epd.width)
# vertical (epd.width, epd.height)
blank_image = Image.new('1', (epd.height, epd.width), 255)
black_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
# display_image(epd, black_image, blank_image)

# epd.sleep()
# epd2in7b.epdconfig.module_exit()
# return lambda: print("Pressed 1")

# string = "The quick brown fox jumps over the lazy dog"
# is_red = False

# x = 10
# y = 10
# size = 14
# fill = 0
# font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)

# display_text(epd, string, is_red, blank_image, x, y, size, fill, font)

snoopy(epd, 0)

btn1.when_pressed = lambda: error(epd, 1)
btn2.when_pressed = lambda: snoopy_red(epd, 2)
btn3.when_pressed = lambda: text_black(epd, 3)
btn4.when_pressed = lambda: text_red(epd, 4)

# btn1.when_pressed = lambda: print(1)
# btn2.when_pressed = lambda: print(2)
# btn3.when_pressed = lambda: print(3)
# btn4.when_pressed = lambda: print(4)

pause()
# input("Press any key")

# Notes:

# # Himage = Image.open(os.path.join(picdir, '2in7.bmp'))
# Himage = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
# epd.display(epd.getbuffer(Himage))
# time.sleep(2)

# epd.Clear()
# black = Image.open(os.path.join(picdir, 'error2in7.bmp'))
# red = Image.open(os.path.join(picdir, 'error2in7_red.bmp'))
# epd.display(epd.getbuffer(black), epd.getbuffer(red))


logging.info("Goto Sleep...")
epd.sleep()