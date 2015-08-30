#!/usr/bin/env python
# coding: utf-8

'''
https://docs.python.org/3/library/threading.html
> Python’s Thread class supports a subset of the behavior of Java’s Thread class;
> currently, there are no priorities, no thread groups, and threads cannot be
> destroyed, stopped, suspended, resumed, or interrupted. The static methods of
> Java’s Thread class, when implemented, are mapped to module-level functions.

https://docs.python.org/3/library/threading.html#thread-objects
> There are two ways to specify the activity: by passing a callable object
> to the constructor, or by overriding the run() method in a subclass.
I selected the first way in this snippet.
'''
import threading
import time
import datetime

def main():
    # http://stackoverflow.com/questions/6524459/stopping-a-thread-after-a-certain-amount-of-time
    # https://docs.python.org/3/library/threading.html#event-objects
    thread_event = threading.Event()
    thread = threading.Thread(target=infiniteLoop_print, args=(3, thread_event))
    thread.start()
    print('[!] {0} started.'.format(thread.getName()))

    # https://docs.python.org/3/library/threading.html#threading.current_thread
    # https://docs.python.org/3/library/threading.html#threading.Thread.getName
    print('[!] {0} started infinite loop.'.format(threading.currentThread().getName()))
    print('[!] The loop will finish if you will press [Ctrl+C].')
    while True:
        try:
            print("[{0}]\t{1}".format(threading.currentThread().getName(), str(datetime.datetime.today())))
            time.sleep(5)
        # https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt
        except KeyboardInterrupt:
            thread_event.set()
            break
    print('[!] The infinite loop of {0} has finished.'.format(threading.currentThread().getName()))

def infiniteLoop_print(waitsec, stop_event):
    while(not stop_event.is_set()):
        # http://qiita.com/konnyakmannan/items/2f0e3f00137db10f56a7
        print("[{0}]\t{1}".format(threading.currentThread().getName(), str(datetime.datetime.today())))
        stop_event.wait(waitsec)
    print('[!] {0} has finished.'.format(threading.currentThread().getName()))

if __name__ == '__main__':
    main()
