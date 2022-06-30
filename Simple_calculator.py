def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print(f"Select Operation")
print(f"1) Addition")
print(f"2) Subtraction")
print(f"3) Multiplication")
print(f"4) Divition")

while True:
    choice = input("Enter choice (1, 2, 3, or 4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print(f" {num1} + {num2} = ", add(num1, num2))
    elif choice == '2':
        print(f" {num1} - {num2} = ", subtract(num1, num2))
    elif choice == '3':
        print(f" {num1} * {num2} = ", multiply(num1, num2))
    elif choice == '4':
        print(f" {num1} / {num2} = ", divide(num1, num2))
    
    next_calculation = input("Let's do another calculation? (yes/no): ")
    if next_calculation == "no":
        break
    
else:
    print("Invalid Input")