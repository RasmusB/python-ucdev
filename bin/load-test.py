#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
To run and test this script, plug CY7C65211 in to the USB port

"""

from __future__ import print_function

import sys, os, platform
import time
from threading import *
from IPython import embed

from ucdev.cy7c65211 import *

if platform.system() == 'Linux':
  dll = "cyusbserial"

elif platform.system() == 'Windows':
  dr = os.path.dirname(__file__)
  # relative path to place .dll in
  dll = os.path.join(dr, 'include/cyusbserial.dll') 

lib = CyUSBSerial(lib = dll)

for i in lib.find(vid=0x04b4, pid=0x0004):
  print(i)

embed()
