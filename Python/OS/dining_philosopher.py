# Define the number of philosophers and forks
NUM_PHILOSOPHERS = 5
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

# Define the Philosopher class
class Philosopher(threading.Thread):
    def __init__(self, index):
        super().__init__()
        self.index = index

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(random.uniform(0, 1))  # Think for a random amount of time

    def eat(self):
        left_fork = forks[self.index]
        right_fork = forks[(self.index + 1) % NUM_PHILOSOPHERS]

        while True:
            if left_fork.acquire(blocking=False):
                if right_fork.acquire(blocking=False):
                    # Philosopher got both forks, can eat now
                    print(f"Philosopher {self.index} is eating.")
                    time.sleep(random.uniform(0, 1))  # Eat for a random amount of time
                    right_fork.release()
                    left_fork.release()
                    break
                else:
                    # Philosopher couldn't get right fork, release left fork
                    left_fork.release()
            # Philosopher couldn't get left fork, try again
            time.sleep(random.uniform(0, 1))

# Create philosopher threads
philosophers = [Philosopher(i) for i in range(NUM_PHILOSOPHERS)]

# Start the threads
for philosopher in philosophers:
    philosopher.start()

# Wait for all threads to finish (not in this example, as they run indefinitely)
# for philosopher in philosophers:
#     philosopher.join()