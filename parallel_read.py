#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-03-01 16:10:05
# Description:测试lock之后,其他线程是否能读到数据

import time
import multiprocessing
import threading


def write(lock,data):
    lock.acquire()
    try:
        i = 0
        while True:
            data["value"] += 1
            time.sleep(5)
            data[i]= "f"
            i += 1
    finally:
        lock.release()

def read(data):
    while True:
        print(data)
        time.sleep(1)

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    data = mgr.dict({"value":0})
    #data = mgr.Value(int,0)
    
    lock = multiprocessing.Lock()

    #processing_count = 1000
    #jobs = [multiprocessing.Process(target = worker,args = (lock,data)) for i in range(processing_count)]

    #for job in jobs:
    #    job.start()

    multiprocessing.Process(target = write,args = (lock,data)).start()

    multiprocessing.Process(target = read,args = (data,)).start()
    
    # 确保每个进程都执行结束 
    time.sleep(60)

    
    print(data["value"])





