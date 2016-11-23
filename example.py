#!/usr/bin/env python3
import sys
import time
import logging
from multiprocessing import Pool
from datetime import datetime, timedelta
from crontab import CronTab

def hoge(self):
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    return 1

p = Pool(2)

p.map(hoge, [1,2,3])

#     # system_cron = CronTab()
#     user_cron = CronTab('9zilla')
#     # mem_cron = CronTab(tab="*/2 * * * * date")
#
#     job = user_cron.new(command='/bin/date')
#     job.hour.every(2)
#     job.enable()
#     print( job.is_valid() )
#
#     user_cron.write('tsl2561.tab')
#
#     tab = CronTab(tabfile='tsl2561.tab')
#
#
# if __name__ == "__main__":  # memo: スクリプトとして直接呼び出した時のみ実行し、別のモジュールから呼び出された時（インポート）には実行しないif文
#
#    main()

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

