# Deliverable Session 01 - Rafael Antonio Echevarria Silva
# c. (1,5) Ask for a number and determine if it is odd or even • Use the modulus operator: “%” • Use conditional statements: “if” & “else”.
# https://www.w3schools.com/python/python_conditions.asp

while True:
    try:
        num = int(input("Enter an integer: "))

        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    again = input("Do you want to enter another number? (yes/no): ").lower()
    if again != 'yes':
        break