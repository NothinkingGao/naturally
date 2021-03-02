#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-03-02 19:15:05
# Description:额,只要活得锁,别的线程就不能继续获取锁
import threading
import time


def fn1(data,lock):
    try:
        target = data.get("key1")
        lock.acquire()
        print("fn1 get the lock.")
        target["value"] +=1
        time.sleep(10)

    finally:
        lock.release()


def fn2(data,lock):
    try:
        lock.acquire()
        print(data)
    finally:
        lock.release()


def run():
    
    data = {
       "key1":{"value":0}
    }

    lock = threading.Lock()
    t1 = threading.Thread(target = fn1,args=(data,lock))
    t2 = threading.Thread(target = fn2,args=(data,lock))

    t1.start()
    t2.start()

    time.sleep(20)


run()





