# Deliverable Session 01 - Rafael Antonio Echevarria Silva
# d. (3) Write a program that shows the divisors of an introduced number. Use “for” statement and use Python list operators.
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.programiz.com/python-programming/list

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
            continue
        divs = [i for i in range(1, num + 1) if num % i == 0]
        print(f"Divisors of {num} are:", divs)
        
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
    again = input("Do you want to enter another number? (yes/no): ").lower()
    if again != 'yes':
        break