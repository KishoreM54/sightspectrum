##----------------threading--------------

import threading

def func(x1,x2,name):
    print("::res1",x1,x2,name)
def func2(x1,x2):
    print("::res2")
x=threading.Thread(target=func,args=(2,4,"res"))
x.start()
x.join()
x=threading.Thread(target=func2,args=(2,6))
x.start()


import threading

def func(x1,x2,name):
    for i in range(x1):
        print("res1->",x1)
def func2(x1,x2):
    for i in range(x2):
        print("res2->")
x=threading.Thread(target=func,args=(5,4,"res"))
x.start()
x.join()
y=threading.Thread(target=func2,args=(2,6))
y.start()
y.join()




import threading
import time

class Class:
    def __init__(self, name):
        self.name = name
    def func(self):
        print(f"Hello, {self.name}!")
def func2():
    for i in range(-1, 6):
        print(i)
        time.sleep(1)
a = Class("John")

x = threading.Thread(target=a.func)
y = threading.Thread(target=func2)
x.start()
y.start()
x.join()
y.join()
print("Done")


import threading
import time

class Class:
    def __init__(self, name):
        self.name = name
    def func(self):
        print(f"Hello, {self.name}!\n")

def func2(x1):
    for i in range(1,6):
        print(i)
        time.sleep(1)
a = Class("John")

x = threading.Thread(target=a.func)
x.start()
x.join()
y = threading.Thread(target=func2,args="3")

y.start()

y.join()
print("\nDone")

import threading
def count(n):
    for i in range(n):
        i+=1
        print(i)
threads = []
for _ in range(3):
    thread = threading.Thread(target=count, args=(5,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()


import threading
import time

class myclass:
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
        
    def func(self):
        print(f"type your enroll ID::")
x=myclass("king","kish")
x.func()

















































































