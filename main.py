import os
import art
#Basic Operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

#Dictionary

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

again = "n"

def calculator():
    print(art.logo)
    num1 = float(input("Enter first number: "))
    for i in operations:
        print(i) 
                       
    while(1):
            
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))
            
        func_name = operations[operation_symbol]
        result = func_name(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
            
        again = input(f"Type 'y' to continue calculating with {result} or Type 'n' to start a new calculation: ")
        if again == "y":
            num1 = result
        else:
            os.system('cls||clear')
            calculator()


calculator()