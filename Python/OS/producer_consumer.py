import threading
import queue
import time
import random

# Define a shared buffer
BUFFER_SIZE = 10
buffer = queue.Queue(BUFFER_SIZE)

# Define a lock for thread synchronization
lock = threading.Lock()

# Define the Producer class
class Producer(threading.Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1, 1000)  # Produce a random item
            with lock:
                if buffer.full():
                    print("Buffer is full. Producer is waiting.")
                    lock.release()
                    time.sleep(random.random())  # Sleep for random time
                    lock.acquire()
                buffer.put(item)
                print(f"Produced {item}.")
                lock.notify()  # Notify waiting consumers
            time.sleep(random.random())  # Sleep for random time

# Define the Consumer class
class Consumer(threading.Thread):
    def run(self):
        global buffer
        while True:
            with lock:
                if buffer.empty():
                    print("Buffer is empty. Consumer is waiting.")
                    lock.release()
                    time.sleep(random.random())  # Sleep for random time
                    lock.acquire()
                item = buffer.get()
                print(f"Consumed {item}.")
                lock.notify()  # Notify waiting producers
            time.sleep(random.random())  # Sleep for random time

# Create producer and consumer threads
producer_thread = Producer()
consumer_thread = Consumer()

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish (not in this example, as they run indefinitely)
# producer_thread.join()
# consumer_thread.join()