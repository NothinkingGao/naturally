#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-03-29 10:13:13
# Description:测试信号处理回调函数是否在独立的线程
# 执行 kill -15 pid查看栈帧情况

import signal
import time
import threading
import traceback
import sys


def my_handler(a,b):
    print(a)
    print(b)
    print(sys._current_frames())

def walk():
    print(sys._current_frames())
    pass

def main():

    signal.signal(signal.SIGTERM, my_handler)
    
    while True:
        thread_num = len(threading.enumerate())
        #print(sys._current_frames())
        time.sleep(2)
        walk()


if __name__ == "__main__":
    main()



