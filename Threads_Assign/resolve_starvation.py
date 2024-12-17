import threading
import time

class FairScheduler:
    def __init__(self):
        self.lock = threading.Lock()

    def execute(self, thread_name):
        with self.lock:
            print(f"{thread_name} is executing")
            time.sleep(1)

scheduler = FairScheduler()

# Threads that use the scheduler
def fair_task(name):
    for _ in range(3):
        scheduler.execute(name)

threadA = threading.Thread(target=fair_task, args=("Thread A",))
threadB = threading.Thread(target=fair_task, args=("Thread B",))

threadA.start()
threadB.start()

threadA.join()
threadB.join()
