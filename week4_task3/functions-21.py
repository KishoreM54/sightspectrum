#### function definition
def find_square(num):
    result = num * num
    return result

### function call
square = find_square(3)

print('Square:',square)
##-------------importing (math,power,sqrt) functions----
import math

square_root = math.sqrt(4)
print("Square Root of 4 is",square_root)
power = pow(2, 3)
print("power of 3 is",power)


##-----------code reusability----------
##
def get(num):
    return num * num
for i in [1,2,3]:
    result = get(i)
    print('Square of',i, '=',result)


def name(val):
    return val*val
for i in [1,2,3,8]:
    result=name(i)
    print('square of',i,'=',result)

##-----------mathamatical expression of different numbers-----

def func(name1,name2,name3):
    sum = name1 + name2 * name3
    return sum
x=func(10,15,2)
print(x)

def get_count(arr,size,target_value):
    cnt=0
    for i in range(0,size):
        if arr[i]==target_value:
            cnt=cnt+1
    return cnt

my_list=[1,2,2,2,2,1,1,1,1,3,3,3,3,4,4,3,3,3,3,3,2,2,2]
print('1 occurance:',get_count(my_list,len(my_list),1))
print('2 occurance:',get_count(my_list,len(my_list),2))
print('3 occurance:',get_count(my_list,len(my_list),3))
print('4 occurance:',get_count(my_list,len(my_list),4))

def generator(n):
    for i in range(n):
        yield i
for num in generator(5):
    print(num)


def number(a):
    for i in range(a):
        yield i
for x in number(10):

    print(x)

##----------------filtering even or odd numbers using generators

def func(value):
    for num in value:
        if num % 2==0:
            yield num
value=[1,2,4,3,5,7,9,6]
result=func(value)
for func in result:
    print(func)





























