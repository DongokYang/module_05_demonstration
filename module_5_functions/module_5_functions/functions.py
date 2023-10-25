"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.
"""
def greet()-> None:
    """
    Prints a greeting meesage to the console.
    Args:
        None
    Returns:
        None
    """
    print("Hello, World!")
 
greet()
greet()
i = 0
while i < 10:
    greet()
    i +=1
 
def greet_name_age(name: str, age: int)-> None:
    """
    Prints a greeting which includes the values of the name and age arguments.
    Args:
        name (str): The name of the person to greet.
        age (str): The age of the person to greet.
    Returns:
        None
    """
    print(f"Hello {name}, you are {age} years old!")
 
greet_name_age("Annie",20)
greet_name_age("Bob", 43)
greet_name("Chris")
greet_name(input("Please input your name: "))
 
def math_operation(operand1: int, operand2: int = 10, operation: str = "+")-> float:
    """
    Returns the result of the specified operation based on the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform, default = "+"
    Returns:
        Float
    Raises:
        ValueError: "Invalid operation." When operation is not + or -.
    """
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")
    return result
 
result = math_operation(1,3,"+")
print(result)
try:
    result = math_operation(6,10,"-")
    print(result)
except ValueError as e:
    print("ERROR: ", e)
try: 
    result = math_operation(5,5,"+")
    print(result)
except ValueError as e:
    print("ERROR: ", e)
 
try: 
    result = math_operation(5,5,"*")
    print(result)
except ValueError as e:
    print("ERROR: ", e)
 
print(math_operation.__doc__)
 
print(input.__doc__)
 
try: 
    result = math_operation(operand2 = 5,operation = "-", operand1 = 20)
    print(result)
except ValueError as e:
    print("ERROR: ", e)