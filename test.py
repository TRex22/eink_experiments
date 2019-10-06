#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
# Display resolution
EPD_WIDTH       = 176
EPD_HEIGHT      = 264

# epd = epd2in7.EPD()
epd = epd2in7b.EPD()
logging.info("init and Clear")
epd.init()
epd.Clear()

font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

blackimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
redimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame

# Himage = Image.open(os.path.join(picdir, '2in7.bmp'))
Himage = Image.open(os.path.join(picdir, '2in7bsnoopy.bmp'))
epd.display(epd.getbuffer(Himage))
time.sleep(2)

epd.Clear()
black = Image.open(os.path.join(picdir, 'error2in7.bmp'))
red = Image.open(os.path.join(picdir, 'error2in7_red.bmp'))
epd.display(epd.getbuffer(black), epd.getbuffer(red))


logging.info("Goto Sleep...")
epd.sleep()