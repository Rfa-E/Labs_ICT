# Deliverable Session 01 - Rafael Antonio Echevarria Silva
# b. (1,5) Ask for your name and surname and save it in different variables. Print them later on the terminal.
# https://www.w3schools.com/python/python_user_input.asp

while True:
    name = input("Enter your name: ")
    last_name  = input("Enter your surname: ")

    print("\nYou entered:")
    print("First name:" + name)
    print("Surname:" + last_name)
    
    again = input("Do you want to enter another name? (yes/no): ").lower()
    if again != 'yes':
        break