#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-02-19 14:22:03
# Description:测试multiprocessing.Manager()的变量是否是线程安全的
# 结论: 不安全,加锁后每次结果都不同,郁闷
import time
import multiprocessing
import threading

def worker(lock,data):
    lock.acquire()
    data["value"] += 1
    lock.release()

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    data = mgr.dict({"value":0})
    #data = mgr.Value(int,0)
    
    lock = multiprocessing.Lock()

    processing_count = 300
    jobs = [multiprocessing.Process(target = worker,args = (lock,data)) for i in range(processing_count)]

    for job in jobs:
        job.start()
    
    print(data["value"])








