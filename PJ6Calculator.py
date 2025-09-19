print("\n")
print(50*"=")
print("Welcome to the simple calculator program")
print(50*"=", "\n")

print(30*"~")
print("Important notes:")
print("(+) for addition")
print("(-) for subtraction")
print("(*) for multiplication")
print("(/) for division")
print(30*"~")

num1 = float(input("\nEnter the first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("The result of", num1, "+", num2, "is", result)
elif operator == "-":
    result = num1 - num2
    print("The result of", num1, "-", num2, "is", result)
elif operator == "*":
    result = num1 * num2
    print("The result of", num1, "*", num2, "is", result)
elif operator == "/":
    result = num1 / num2
    print("The result of", num1, "/", num2, "is", result)
else:
    print("Error: Please enter input according to the instructions!")

print("End of the simple calculator program")
