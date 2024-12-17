import threading
import time

def low_priority():
    while True:
        print("Low priority thread running")
        time.sleep(0.1)

def high_priority():
    while True:
        print("High priority thread running")
        time.sleep(0.01)

# Create threads
low_thread = threading.Thread(target=low_priority)
high_thread = threading.Thread(target=high_priority)

# Make the high-priority thread daemon
high_thread.setDaemon(True)

low_thread.start()
high_thread.start()

# Let it run for 3 seconds
try:
    time.sleep(3)
except KeyboardInterrupt:
    pass
