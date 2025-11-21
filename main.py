first_number = input("Enter the first number: ")
selected_operation = input("Select an operation (+, -, *, /): ")
second_number = input("Enter the second number: ")

if selected_operation == "+":
    result = float(first_number) + float(second_number)
    print(f"The result is: {result}")
elif selected_operation == "-":
    result = float(first_number) - float(second_number)
    print(f"The result is: {result}")
elif selected_operation == "*":
    result = float(first_number) * float(second_number)
    print(f"The result is: {result}")
elif selected_operation == "/":
    if float(second_number) != 0:
        result = float(first_number) / float(second_number)
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation selected.")

# This is a simple calculator program that performs basic arithmetic operations based on user input.
# It prompts the user to enter two numbers and select an operation, then computes and displays the result.