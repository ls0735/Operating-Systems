import threading
import time

def count_up(name):
    for i in range(1, 6):
        print(f"{name}: {i}")
        time.sleep(1)  # Sleep for 1 second between counts

# Create two threads
thread1 = threading.Thread(target=count_up, args=("Thread 1",))
thread2 = threading.Thread(target=count_up, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Program completed.")

