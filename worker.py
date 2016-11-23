#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import signal
import time

import oursql
import yaml
f = open("database.yml", 'r')
db = yaml.load(f)
f.close()

from datetime import datetime
from multiprocessing import Process, Queue, Event

sys.path.append("TSL2561")
from TSL2561 import *
tsl = TSL2561()

INTERVAL_SEC = 60 * 5

##############################
### Sub processes          ###
##############################
class SubProcess(object) :

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

    def saveLux(self):
        with oursql.connect(
                host=db["host"],
                port=db["port"],
                db=db["name"],
                user=db["user"],
                passwd=db["pass"]).cursor() as cur:

            now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            lux = str(self.getLux())

            sql = "insert into " + db["name"] +".luxes" \
                    " (recorded_at, lux, created_at, updated_at)" \
                    " values" \
                    " ('"+now+"',"+lux+",'"+now+"','"+now+"')"
            res = cur.execute(sql)
        return res

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

            self.saveLux()

            time.sleep(INTERVAL_SEC)

        print( "Stop subprocess..." )


##############################
### Main                   ###
##############################
if __name__ == '__main__' :

	if tsl.foundSensor():
		print("Found sensor...")

		### Queue
		inc_q = Queue()
		mul_q = Queue()

		### Event
		stop_flag = Event()


		### Sub processes
		sub1 = SubProcess()

		sub1_process = Process(target = sub1.run, args = (inc_q, stop_flag))

		### Start sub processes
		# processes = [sub1_process, sub2_process, sub3_process]
		processes = [sub1_process]
		for p in processes :
			p.start()

		### Signal settings
		def signalHandler(signal, handler) :
			stop_flag.set()

		signal.signal(signal.SIGINT,  signalHandler)
		signal.signal(signal.SIGTERM, signalHandler)

		### Wait subprocess stop
		while True :
			alive_flag = False
			for p in processes :
				if p.is_alive() :
					alive_flag = True
					break
			if alive_flag :
				time.sleep(0.1)
				continue
			break

		print( "Complete !!!" )

	else:
		print("No sensor?")
