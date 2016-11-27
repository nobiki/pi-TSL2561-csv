#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import signal
import time
import base64

import oursql
import yaml
f = open(os.path.dirname(__file__)+"/database.yml", 'r')
db = yaml.load(f)
f.close()

import pandas as pd
import matplotlib as plt
plt.use('Agg')

from datetime import datetime
# from multiprocessing import Process, Queue, Event

sys.path.append(os.path.dirname(__file__)+"/TSL2561")
from TSL2561 import *
tsl = TSL2561()

INTERVAL_SEC = 60 * 5

##############################
### TSL2561Logger Class
##############################
class TSL2561Logger() :

    def __init__(self) :
        self.first = 0
        self.step  = 1

    def getLux(self):
        tsl.setGain(tsl.GAIN_16X);
        tsl.setTiming(tsl.INTEGRATIONTIME_13MS)

        x = tsl.getFullLuminosity()
        full = tsl.getLuminosity(tsl.FULLSPECTRUM)
        visible = tsl.getLuminosity(tsl.VISIBLE)
        infrared = tsl.getLuminosity(tsl.INFRARED)

        # print("Lux: %d" % tsl.calculateLux(full, infrared) )
        lux = tsl.calculateLux(full, infrared)
        return lux

    def saveLuxData(self):
        conn = oursql.connect(
                host=db["host"],
                port=db["port"],
                db=db["name"],
                user=db["user"],
                passwd=db["pass"])
        self.saveLux2Database(conn)
        self.saveLux2Graph(conn)

    def saveLux2Graph(self,conn):
        cur = conn.cursor()

        # Output Graph image
        sql = "select recorded_at, lux from luxes order by recorded_at desc limit 288"

        df = pd.read_sql(sql,conn)

        df.plot(x='recorded_at')
        plt.pyplot.savefig(os.path.dirname(__file__)+"/luxes.png")

        # insert binary(base64)
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        graphfile = open(os.path.dirname(__file__)+"/luxes.png", 'rb').read()
        graph64 = base64.b64encode(graphfile).decode('utf-8')

        sql = "update " + db["name"] +".graphs" \
                " set" \
                " graph64 = '"+graph64+"'," \
                " updated_at = '"+now+"' where id = 1"

        cur.execute(sql)

    def saveLux2Database(self,conn):
        cur = conn.cursor()

        # insert lux(from pi)
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        lux = str(self.getLux())

        sql = "insert into " + db["name"] +".luxes" \
                " (recorded_at, lux, created_at, updated_at)" \
                " values" \
                " ('"+now+"',"+lux+",'"+now+"','"+now+"')"

        cur.execute(sql)

    def run(self, inc_q, stop_flag) :

        ### Signal disable
        signal.signal(signal.SIGINT,  signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)

        print( "Start subprocess..." )

        count = 0
        while True :
            if stop_flag.is_set() :
                break
            count += 1
            inc_q.put(self.first + self.step * count)

            # debug print
            print( datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ": " + str(self.getLux()) )

            self.saveLuxData()

            time.sleep(INTERVAL_SEC)

        print( "Stop subprocess..." )

