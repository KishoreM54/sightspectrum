##-----------break-------------
x=int(input("how many candies you want?"))
i=1
while i<=x:
    print("candy")
    i+=1

available_candy=7
x=(int(input("how many candies you want?")))
i=1
while i <= x:
    
    if i > available_candy:
        print("out of stock")
        break
    print("candy")
    i+=1
print("bye bye")

for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)
print("bye")

##------------no odd numbers--------

for i in range(1,101):
    if i%2 != 0:
        pass
    else:
        print(i)

print("bye")

##---i want result as"kishoresubscribesubscribesubscribesubscribe" 4times-----
##nested while loop
i=1
##
while i<=4:
    print("kishore",end="")
    k=1
    while k<=4:
        print("subscribe",end="")
        k += 1
    i += 1
    print()
##    

##---#if statement--------
amount=600
if amount>500:
    discount=0.3*amount if amount>500 else 0
    print(discount)

if 6>11:
    print("six is lesser than eleven")

else:
    print("bye bye")

x=3
y=4
if x <= y:
    print("number_1")
elif x==y:
    print("number_2")
else:
    print("number_3")
print("bye")


x=int(input("your home loan is ?"))
y=int(input("your fine amount"))
print(y)
if x>1000:
    y=0.1*x if x > 1000 else 0
    a= x + y
    print(a)
i=45
while i<10:
    print(i)
    i+=1
else:
    print("dance with kishore")
    
fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)
    if i == "banana":
       break

number=[1,3,5,7,9]
for i in number:
    print(i)
    if i == 5:
        break
##        
##-------break statement-----
##
name="kishore"
for i in name:
    print(i)
    if i == "o":
        break
##----continue statement-------
i=0
a="anjalipapa"
while i<len(a):
    if a[i]=="a" or a[i]=="p":
        i += 1
        continue
    print("its over:",a[i])
    i+=1
         
n=int(input("number of stars:"))
for i in range(n):
##    print("*")
    print("*",end="")
















































