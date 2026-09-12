class Calculator:
    def add(self , a , b):
        sum = a + b
        print(f"\nThe sum of {a} and {b} is {sum}\n \n")
    def subtract(self , a , b):
        subtract = a - b
        print(f"\nThe subtraction  of {a} and {b} is {subtract}\n \n")
    def multipliction(self, a, b):
        multipliction = a * b
        print(f"\nThe multipliction  of {a} and {b} is {multipliction}\n \n")
    def division(self, a, b):
        try:
            division = a / b
            print(f"\nThe division  of {a} and {b} is {division}\n \n")
        except ZeroDivisionError:
            print("You cannot divide any number by zero!")

calculate = Calculator()
while True:
    print("---------Welcome to the calculator---------")
    print("1. Additon")
    print("2. subtraction")
    print("3. multipliction")
    print("4. division")
    
    source = int(input("Please select any option between 1-4:"))
    match source:
        case 1:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            calculate.add(a,b)
        case 2:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            calculate.subtract(a,b)
        case 3:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            calculate.multipliction(a,b)
        case 4:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            calculate.division(a,b)
        case _:
            print("!!!!!!!Please any a valid option!!!!!!!\n")
