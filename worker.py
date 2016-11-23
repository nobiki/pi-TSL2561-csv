#!/usr/bin/env python3
import sys
import time
import logging
import multiprocessing
from datetime import datetime, timedelta
from crontab import CronTab

def worker(num):
    """worker function"""
    print("Worker " + str(i) + " start.")
    time.sleep(i*2)
    print("Worker " + str(i) + " end. - " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker,args=(i,))
        jobs.append(p)
        p.start()
