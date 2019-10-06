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

font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
font12 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Regular.ttf'), 12)

blackimage = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)  # 255: clear the frame
redimage = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)  # 255: clear the frame

# Text
x = 25
y = 65
size = 12
fill = 0
font = font12

def init_epd():
  # epd = epd2in7.EPD() # B/W only
  epd = epd2in7b.EPD() # B/W/R
  logging.info("init and Clear")
  epd.init()
  epd.Clear()
  return epd

def display_image(epd, black_image, red_image):
  epd.display(epd.getbuffer(black), epd.getbuffer(red))
  epd.sleep()

def display_text(epd, string, is_red, blank_image, x, y, size, fill, font):
  image = ImageDraw.Draw(blank_image)

  draw.text((x, y), string, font = font, fill = 0)

  if (is_red == true):
    epd.display(epd.getbuffer(blank_image), epd.getbuffer(image))
  else:
    epd.display(epd.getbuffer(image), epd.getbuffer(image))

def process_button(btn):
  pin = btn.pin.number
  epd = init_epd()

  blank_image = Image.new('1', (epd.width, epd.height), 255)

  # 5, 6, 13, 19
  if (pin == 5):
    black_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
    display_image(epd, black_image, blank_image)
  if (pin == 6):
    red_image = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
    display_image(epd, blank_image, red_image)
  if (pin == 13):
    string = "The quick brown fox jumps over the lazy dog"
    is_red = False

    x = 25
    y = 65
    size = 12
    fill = 0
    font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Regular.ttf'), 12)

    display_text(epd, string, is_red, blank_image, x, y, size, fill, font)
  if (pin == 19):
    string = "The quick brown fox jumps over the lazy dog"
    is_red = True

    x = 25
    y = 65
    size = 12
    fill = 0
    font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Regular.ttf'), 12)

    display_text(epd, string, is_red, blank_image, x, y, size, fill, font)

  epd.sleep()
  epd2in7b.epdconfig.module_exit()
  exit()

btn1.when_pressed = process_button
btn2.when_pressed = process_button
btn3.when_pressed = process_button
btn4.when_pressed = process_button

# Notes:

# # Himage = Image.open(os.path.join(picdir, '2in7.bmp'))
# Himage = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
# epd.display(epd.getbuffer(Himage))
# time.sleep(2)

# epd.Clear()
# black = Image.open(os.path.join(picdir, 'error2in7.bmp'))
# red = Image.open(os.path.join(picdir, 'error2in7_red.bmp'))
# epd.display(epd.getbuffer(black), epd.getbuffer(red))


# logging.info("Goto Sleep...")
# epd.sleep()