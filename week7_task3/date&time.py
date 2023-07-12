##----------how to find date and time----------
import datetime

x = datetime.datetime.now()

print(x)

print(type(x))

y=x.strftime("%A")
print(y)
print(x.strftime("%A"))    #%A-find current day within a week


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%B")) #%B-find current month

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%C"))  #C-find current date


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A","%B","%C")) 

import datetime

x = datetime.datetime.now()

##print(x)
print(x.strftime("%c"))

print(type(x))



import datetime

x= datetime.datetime.now()

y = x.strftime("%Y-%m-%d %H:%M:%S")

print(f"currentD&T: {y}")

from datetime import datetime
##import

x=now.replace(microsecond=0)
print(x)

y = x.strftime("%Y-%m-%d %H:%M:%S")
y=x.strftime("%d/%b/%Y/%I:%M-%p")
z=x.strftime("%H:%M")


print(f"current D:: {y}\ncurrent T:: {z} ")
print(type(z))

import datetime

x= datetime.datetime.now()
y=x.strftime("%d/%m/%Y")
print(y)

x1 = y.weekday() 
print(x1)
import datetime  
from datetime import datetime
x=datetime.now()
print(x)
y=x.replace(microsecond=0)
print(y)

import datetime
##from datetime import datetime
x=datetime.datetime.now()
print(x)
add_hrs=5
y= x+ datetime.timedelta(hours=add_hrs)
y1=y.replace(microsecond=0)
z1=x.weekday()
print(y1)
print(z1)

import datetime
x=datetime.datetime.now()
print(x)
add_hrs=5
y= x+ datetime.timedelta(hours=add_hrs)
y1=y.replace(microsecond=0)
z1=x.timestamp()
print(y1)
print(z1)

import calendar
x=calendar.month(2023,7)
print(x)

import calendar
x=calendar.prcal(2023,7)
print(x)

import calendar
import datetime
a=datetime.datetime.now()
b=a.weekday()
x=calendar.month(2023,8)
print(y)

import calendar
import datetime
from calendar import datetime
a = datetime.datetime.now()
b = a.weekday()
print(b)
x = calendar.month(2023,7,22)

print(x)










































