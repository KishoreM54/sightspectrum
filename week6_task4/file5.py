####exception handling-------

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")




try:
    print("x")
except:
    print("hellloooo")
finally:
    a=3+6
    print(a)


try:
    print(x)
except:
    print("error")
    
finally:
    a=3+6
    print(a)
try:
    var=(10/0)
    print(var)
except:
    print("helllo")


try:
    a="3"+9
    print(a)
except:
    print("it's correct or not")

##
try:
    var=105/0
    print(var1)
except ZeroDivisionError as var:
    print(var)
except TypeError as var:
    print(var)
except:
    print("hjf")


try:
    a=1,0,3
    print(a2)

except TypeError:
    print("bye")


try:
    b=30.4/0
    print(b)
except ZeroDivisionError as b:
    print(b)

except:
    print("true or false")




try:
    x=0%0
    print(x)
except TypeError as a:
    print("do work")


try:
    z="3=6"
    print(z)
except ZeroDivisionError as x:
    print("false")




















##try:
##    a=int(input("enter the number:"))
##    print("anything:",a)

