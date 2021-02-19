#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-01-25 19:51:45
# Description:some description
import threading
import time

def target(data,thread_index):
    while True:
        print("thread_{}:{}".format(thread_index,data))
        time.sleep(1)

def run():
    data = {}

    results = list()
    for i in range(3):
        t = threading.Thread(target=target,args=(data,i))
        results.append(t)
    
    for item in results:
        item.start()
    
    for i in range(3):
        data.update({"{}_main_thread".format(i):i})
        time.sleep(1)

run()
