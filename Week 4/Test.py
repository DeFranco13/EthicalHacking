import threading
from time import sleep

def function1():
    for i in range(10):
        print(f"Function 1: Step {i + 1}")
        sleep(1)  # Simulate some work

def function2():
    for i in range(10):
        print(f"Function 2: Step {i + 1}")
        sleep(1)  # Simulate some work

if __name__ == "__main__":
    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()