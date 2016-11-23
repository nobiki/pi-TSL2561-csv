#!/usr/bin/env python3
import sys
import time
import logging

from datetime import datetime, timedelta
from crontab import CronTab


def main():
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    # # 処理2を２分毎に実行する。
    cron_2min = CronTab("*/2 * * * *")

    print(dir(cron_2min))

    cron_2min.next()

if __name__ == "__main__":  # memo: スクリプトとして直接呼び出した時のみ実行し、別のモジュールから呼び出された時（インポート）には実行しないif文

   main()

### quickwire-i2c
# sys.path.append("TSL2561")
#
# from TSL2561 import *
# from TSL2561_logger import *
#
#
# tsl = TSL2561()
# logger = TSL2561_logger()


### DB参照
# def sample_oursql():
#     import oursql
#     with oursql.connect(
#             host='my-gandamu',
#             db='tsl2561_stats_development',
#             user='9zilla',
#             passwd='9zilla').cursor() as cur:
#
#         cur.execute('SELECT * FROM luxes')
#         res = cur.fetchall()
#
#         for row in res:
#             print(row[2])
#
#
# sample_oursql()

### tsl2561
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

