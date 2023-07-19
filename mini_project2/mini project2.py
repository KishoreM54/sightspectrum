
##Simple Calculator: Build a calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.

expression = input("Enter your need: ")
result = eval(expression)
print("Result:", result)



## Before modifying code:

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Div by 0 is not allowed"

while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        break
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = sub(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = mul(num1, num2)
        print("Result:", result)
    elif choice == '4':
        result = div(num1, num2)
        print("Result:", result)
    else:
        print("Result:",result)
##
####After modified code simple calculator works in perfect flow:

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Div by 0 is not allowed"

result = 0
print('Simple calculator')

while True:
    if result == 0:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    else:
        num1 = result

    print("Select an operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Use the current result for further calculations")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice != '5':
      result = 0

    if choice == '6':
        break

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid choice. Please select a valid operation.")
        continue

    if choice == '5':
      num2 = float(input("Enter the next number: "))
      continue

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = sub(num1, num2)
    elif choice == '3':
        result = mul(num1, num2)
    elif choice == '4':
        result = div(num1, num2)

    print("Result:", result)

##using algorithm
    
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else None

def calculate(result=0.0):
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Use the current result for further calculations")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Final result:", result)
        print("Calculator quitting...")
        return

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operation = None
        if choice == '1':
            operation = add
        elif choice == '2':
            operation = subtract
        elif choice == '3':
            operation = multiply
        elif choice == '4':
            operation = divide

        if operation is not None:
            result = operation(num1, num2)
            if result is not None:
                print("Result:", result)
    elif choice == '5':
        num = float(input("Enter the next number: "))
        result = add(result, num)
        print("Result:", result)
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

    calculate(result) 
calculate() 

    
        








































        
























