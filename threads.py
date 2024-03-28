import threading
import time

def my_function():
    print("This is my thread")

my_thread = threading.Thread(target = my_function)

my_thread.start()

my_thread.join()

#simple example
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# Create a thread
my_thread = threading.Thread(target=print_numbers)

# Start the thread
my_thread.start()

# Do something else in the main thread
print("Main thread is doing something else")


#wait for the thread to finish
my_thread.join()

print("Thread has finished")