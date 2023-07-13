
import datetime
x=datetime.datetime.now()
print(x)
y=x.replace(microsecond=0,second=0,minute=0)
print(y)
z=y.weekday()
print(z)
y1=x.strftime(f"%d/%m/%Y")
y1=x.strftime(f"%d/%m/%Y %d-%B-%Y %d-%b-%y")
print(y1)
add_hours=5

y2=x+ datetime.timedelta(hours=add_hours)
print(y2)



import threading
import time
def func(name,y):
    print(f"hai {name} your ID no. is {y}")
    time.sleep(2)
def func1(name,y):
    print(f"hai {name} your ID no. is {y}")
    time.sleep(3)
def func2(name,y):
    print(f"hai {name} your ID no. is {y}")
x1=threading.Thread(target=func,args=("kishore",11455))
y1=threading.Thread(target=func1,args=("gopi",11454))
z1=threading.Thread(target=func1,args=("divya",11456))
x1.start()
x1.join()
y1.start()
y1.join()
z1.start()
##z1.join()


import concurrent.futures
def func(self):
    print("please wait .. ..")
    print(f"processing : {self}\n")
self=[1,2,3,4,5]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(func,self)

import concurrent.futures

def func(element):
    print("please wait...")
    print(f"processing: {element}\n")

elements = [1, 2, 3, 4, 5]

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(func, elements)

y=[2,3,5,6,9]
result=map(lambda x: x * 2,y)
print(list(result))

numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2,numbers))
print(doubled_numbers)

def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))

import threading
x=5
def increment():
    for i in range(5):
        global x
        x += 1
    print("increment:", x)
def decrement():
    for i in range(5):
        global x
        x -= 1
    print("decrement:", x)
    
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)
thread1.start()
thread1.join()
thread2.start()
thread2.join()






















































