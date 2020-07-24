import threading
import os
import test1
import test2


def thread_1(n):
    os.system('cmd /k "date" ')


def thread_2(n):
    os.system('cmd /k "color a & date" ')


t1 = threading.Thread(target=thread_1, args=(10,))
t2 = threading.Thread(target=thread_2, args=(10,))

t1.start()
t2.start()

t1.join()
print("Thread 1")
t2.join()
print("Thread 2")

print("complete")
