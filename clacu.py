def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    print("Simple Calculator")
    
    try:
        # Prompt the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Prompt the user to choose an operation
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter the number corresponding to the operation: ")
        
        # Perform the calculation based on user input
        if operation == '1' or operation == '+':
            result = add(num1, num2)
            operation_sign = '+'
        elif operation == '2' or operation == '-':
            result = subtract(num1, num2)
            operation_sign = '-'
        elif operation == '3' or operation == '*':
            result = multiply(num1, num2)
            operation_sign = '*'
        elif operation == '4' or operation == '/':
            result = divide(num1, num2)
            operation_sign = '/'
        else:
            result = "Error: Invalid operation selected."
            operation_sign = ''
        
        # Display the result
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} {operation_sign} {num2} = {result}")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
