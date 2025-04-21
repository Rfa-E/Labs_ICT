# Deliverable Session 01
# a. (1) Create your first “helloworld”, print it on the terminal.
# https://www.w3schools.com/python/python_intro.asp

print("helloworld")

# b. (1,5) Ask for your name and surname and save it in different variables. Print them later on the terminal.
# https://www.w3schools.com/python/python_user_input.asp

name = input("Enter your name: ")
sname  = input("Enter your surname: ")

print("\nYou entered:")
print("First name:" + name)
print("Surname:" + sname)

# c. (1,5) Ask for a number and determine if it is odd or even • Use the modulus operator: “%” • Use conditional statements: “if” & “else”

n = int(input("Enter an integer: "))

if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")