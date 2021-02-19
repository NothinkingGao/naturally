#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-02-19 14:22:03
# Description:测试multiprocessing.Manager()的变量是否是线程安全的
# 结论: 不安全,加锁后每次结果都不同,郁闷,原因是因为有的进程没有执行结束
import time
import multiprocessing
import threading

def worker(lock,data):
    lock.acquire()
    try:
        data["value"] += 1
    finally:
        pass
        lock.release()

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    data = mgr.dict({"value":0})
    #data = mgr.Value(int,0)
    
    lock = multiprocessing.Lock()

    processing_count = 1000
    jobs = [multiprocessing.Process(target = worker,args = (lock,data)) for i in range(processing_count)]

    for job in jobs:
        job.start()
    
    # 确保每个进程都执行结束 
    time.sleep(2)

    
    print(data["value"])








