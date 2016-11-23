#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import time

from multiprocessing import Process, Queue, Event

INTERVAL_SEC = 2

##############################
### Sub processes          ###
##############################
class SubProcess(object) :

    def __init__(self) :
        self.first = 0
        self.step  = 1

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

            time.sleep(INTERVAL_SEC)
            print("Executing subprocess...")

        print( "Stop subprocess." )

##############################
### Main                   ###
##############################
if __name__ == '__main__' :

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
