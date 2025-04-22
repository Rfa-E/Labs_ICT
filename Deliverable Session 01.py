# Deliverable Session 01 - Rafael Antonio Echevarria Silva
# a. (1) Create your first “helloworld”, print it on the terminal.
# https://www.w3schools.com/python/python_intro.asp

print("helloworld   \n")

# b. (1,5) Ask for your name and surname and save it in different variables. Print them later on the terminal.
# https://www.w3schools.com/python/python_user_input.asp

name = input("Enter your name: ")
sname  = input("Enter your surname: ")

print("\nYou entered:")
print("First name:" + name)
print("Surname:" + sname)

# c. (1,5) Ask for a number and determine if it is odd or even • Use the modulus operator: “%” • Use conditional statements: “if” & “else”.

n = int(input("Enter an integer: "))

if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")
    
# (3) Write a program that shows the divisors of an introduced number. Use “for” statement and use Python list operators.
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.programiz.com/python-programming/list

num = int(input("Enter a positive integer: "))
divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print(f"Divisors of {num} are:", divisors)

#e. (3) Check if a word introduced is a palindrome. Use “if” statement.
# https://www.w3schools.com/python/python_strings_methods.asp

word = input("Enter a word: ").strip()

# normalize case so 'Level' counts as palindrome too
normalized = word.lower()

if normalized == normalized[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
