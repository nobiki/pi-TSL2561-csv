#!/usr/bin/env python3
import time
import multiprocessing

def worker(num):
    """worker function"""
    print("Worker " + str(i) + " start.")
    time.sleep(i*2)
    print("Worker " + str(i) + " end.")
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker,args=(i,))
        jobs.append(p)
        p.start()
