import threading
import time

# Create two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    lock1.acquire()
    print("Task1 acquired lock1")
    time.sleep(1)
    lock2.acquire()
    print("Task1 acquired lock2")
    lock2.release()
    lock1.release()

def task2():
    lock2.acquire()
    print("Task2 acquired lock2")
    time.sleep(1)
    lock1.acquire()
    print("Task2 acquired lock1")
    lock1.release()
    lock2.release()

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
