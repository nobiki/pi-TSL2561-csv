#!/usr/bin/env python3
import sys
sys.path.append("TSL2561")

from TSL2561 import *

tsl = TSL2561()

if tsl.foundSensor():
    print("Found sensor...")

    tsl.setGain(tsl.GAIN_16X);
    tsl.setTiming(tsl.INTEGRATIONTIME_13MS)

    x = tsl.getFullLuminosity()
    full = tsl.getLuminosity(tsl.FULLSPECTRUM)
    visible = tsl.getLuminosity(tsl.VISIBLE)
    infrared = tsl.getLuminosity(tsl.INFRARED)

    print("Lux: %d" % tsl.calculateLux(full, infrared) )
else:
    print("No sensor?")

