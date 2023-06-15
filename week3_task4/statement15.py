#Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

# Python program to illustrate
 #Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)
##
### Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)
##
### Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
	print(i)
##
# Iterating over dictionary
##print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))

### Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),

height=int(input("enter the height:"))
width=int(input("enter the width:"))
for i in range(height):
    for j in range(width):
        print("gayu",end="")
    print()

##-----------lambda function---------
def add(x,y):
    return x+y
print(add(1,3))

##for replacing this addition in simple format!
a=lambda x,y : x+y  #----------+
print(a(1,3))
b=lambda x,y,z : (x+y)*z    #---------*
print(b(1,3,6))

b=lambda x,y,z : (x+y)/z #------/
print(b(1,3,6))

b=lambda x,y,z : x*y*z
print(b(1,3,6))

x=lambda a,b,c,d,e : ((a*b)/(c+d+e))*e
print(int(x(2,4,6,8,10)))

import random

secret_number = random.randint(1, 100)
attempts = 0
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")

start = 1
end = 100

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
student_scores = {"John": 85, "Emma": 92, "Ryan": 78, "Sophia": 95}

for name, score in student_scores.items():
    print(f"{name} scored {score}")
num = 2
total_sum = 0

while num <= 100:
    total_sum += num
    num += 2
print("Sum of even numbers:", total_sum)

num = 6
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)













































    

