#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import signal
import time

from datetime import datetime
from multiprocessing import Process, Queue, Event

sys.path.append(os.path.dirname(__file__)+"/TSL2561")
from TSL2561 import *
tsl = TSL2561()

from TSL2561Logger import *

##############################
### Main
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
		sub1 = TSL2561Logger()

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
