##-----------for loop-----------
sum=0
for i in range(10):
    sum=sum+i
    print(sum)
##----------print letter by letter-----
word="anaconda"
for letter in word:
    print(letter)


for i in range(10):
    print(i)
a=["apple","doctor","patient"]
for element in a:
     print(element) 

a=["apple","doctor","patient"]
for i in range(3):
    #or
for i in range(len(a)):
    print(a[i])

##-------wanna type a single element multiple times- 

for i in range(len(a)):
    for j in range(i+1):
        print(a[i])
#qstn: can you compte the sum of all multiples of 3 and 5 that are less than 100?
print(list(range(1,100)))
total=0
for i in range(1,100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)
total=0
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        print(total)

##sum of al negative numbers?
my_list=[10,13,15,-3,-2,-9,-18]
y=my_list.sort()

my_list=[8,4,4,3,1,0,-3,-5,-9]
total = 0
a = len(my_list) - 1
while my_list[a] < 0:
    total += my_list[a]
    a -= 1
print(total)

number=int(input("enter an integer:"))
for count in range(1,20):
    product = number*count
    print(number,"*",count,"=",product)

##canyou create a program to find the sum of numbers from 1 to 100?
result=1+2+3+....+100
print(list(range(1,101)))
number=int(input("sum of number:"))
for total in range(1,101):
    answer= number+total
    print(number,"+",total,"=",answer)
    print(answer2,"+",total,"=",answer)
number=0
for i in range(0,101):
    number += 1
    print(number)
i=0
sum=0
for i in range(1,101):
    sum = (i,end="'")
    i += 1
    print(sum)
    
x=[2,4,0,-4,-3,-6]
for i in range(1,101):
numbers=[4,5,6,7,8,9,10,11,12,13,14,15,16,17]
sums=[0] * (len(numbers)+1)
for i in range(len(numbers) ):
    sums[i+1] = sums[i]+numbers[i]
rangesum = sums[20] - sums[5]
print(rangesum)

num=(1,2,4,7)
sums = 0
for nums in num:
    nums = nums + num
print(f"sum of numbers is{nums}")

nums = (1, 2, 3, 4)

sum_nums = 0

for num in nums:
    sum_nums = sum_nums + num

print(f'Sum of numbers is {sum_nums}')

 Output
 Sum of numbers is 10

for x in range(3):
    print("printing:",x)

nums = [1, 2, 3, 4, 5, 6]

n = 2

found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')

 Output
 List contains 2: True

print("print('what is print')")







    





    































