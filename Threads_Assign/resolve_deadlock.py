import threading
import time

# Create two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def task1_resolved():
    with lock1:
        print("Task1 acquired lock1")
        time.sleep(1)
        with lock2:
            print("Task1 acquired lock2")

def task2_resolved():
    with lock1:
        print("Task2 acquired lock1")
        time.sleep(1)
        with lock2:
            print("Task2 acquired lock2")

# Create threads
thread1_resolved = threading.Thread(target=task1_resolved)
thread2_resolved = threading.Thread(target=task2_resolved)

thread1_resolved.start()
thread2_resolved.start()

thread1_resolved.join()
thread2_resolved.join()
