#!/usr/bin/env python3
import sys
import time
import logging

from datetime import datetime, timedelta
from crontab import CronTab

# sys.path.append("TSL2561")
#
# from TSL2561 import *
# from TSL2561_logger import *
#
#
# tsl = TSL2561()
# logger = TSL2561_logger()

def sample_oursql():
    import oursql
    with oursql.connect(
            host='my-gandamu',
            db='tsl2561_stats_development',
            user='9zilla',
            passwd='9zilla').cursor() as cur:

        cur.execute('SELECT * FROM luxes')
        res = cur.fetchall()

        for row in res:
            print(row[2])


sample_oursql()

# if tsl.foundSensor():
#     print("Found sensor...")
#
#     tsl.setGain(tsl.GAIN_16X);
#     tsl.setTiming(tsl.INTEGRATIONTIME_13MS)
#
#     x = tsl.getFullLuminosity()
#     full = tsl.getLuminosity(tsl.FULLSPECTRUM)
#     visible = tsl.getLuminosity(tsl.VISIBLE)
#     infrared = tsl.getLuminosity(tsl.INFRARED)
#
#     logger.hello()
#
#     print("Lux: %d" % tsl.calculateLux(full, infrared) )
# else:
#     print("No sensor?")

