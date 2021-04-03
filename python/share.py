#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-01-25 11:11:55
# Description:管理进程间的状态
import time
import multiprocessing

def worker(dictionary,key,item):

    while True:
        print(dictionary)
        dictionary[key] = item
        time.sleep(1)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    
    jobs = [multiprocessing.Process(target = worker,args = (dictionary,i,i*2)) for i in range(3)]

    for job in jobs:
        job.start()

    #for job in jobs:
    #    job.join()

    while True:
        for i in range(10):
            dictionary["main_{}".format(i)] = i
            time.sleep(2)
    
