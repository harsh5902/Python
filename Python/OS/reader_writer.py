import threading
import time

# Define a lock for thread synchronization
lock = threading.Lock()

# Define variables to track the number of readers and writers
readers_count = 0
writers_count = 0

# Define the shared resource
shared_resource = "Initial Value"

# Define the Reader class
class Reader(threading.Thread):
    def run(self):
        global readers_count
        global shared_resource

        # Acquire the lock before reading
        with lock:
            readers_count += 1
            if readers_count == 1:
                # First reader, lock the resource to writers
                print("First reader. Locking resource to writers.")
                shared_resource = "Locked by reader"
        lock.release()

        # Read from the shared resource
        print(f"Reader {self.ident} reads: {shared_resource}")

        # Acquire the lock to update readers count
        with lock:
            readers_count -= 1
            if readers_count == 0:
                # No readers left, unlock the resource
                print("No readers left. Unlocking resource.")
                shared_resource = "Unlocked"
        lock.release()

# Define the Writer class
class Writer(threading.Thread):
    def run(self):
        global writers_count
        global shared_resource

        # Acquire the lock before writing
        with lock:
            writers_count += 1
            if writers_count == 1:
                # First writer, lock the resource to readers
                print("First writer. Locking resource to readers.")
                shared_resource = "Locked by writer"
        lock.release()

        # Write to the shared resource
        new_value = f"New Value written by {self.ident}"
        print(f"Writer {self.ident} writes: {new_value}")
        shared_resource = new_value

        # Acquire the lock to update writers count
        with lock:
            writers_count -= 1
            if writers_count == 0:
                # No writers left, unlock the resource
                print("No writers left. Unlocking resource.")
                shared_resource = "Unlocked"
        lock.release()

# Create reader and writer threads
readers = [Reader() for _ in range(5)]
writers = [Writer() for _ in range(2)]

# Start the threads
for reader in readers:
    reader.start()
for writer in writers:
    writer.start()

# Wait for all threads to finish (not in this example, as they run indefinitely)
# for reader in readers:
#     reader.join()
# for writer in writers:
#     writer.join()
