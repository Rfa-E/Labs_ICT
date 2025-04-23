# Deliverable Session 01 - Rafael Antonio Echevarria Silva
# e. (3) Check if a word introduced is a palindrome. Use “if” statement.
# https://www.w3schools.com/python/python_strings_methods.asp

while True:
    word = input("Enter a word: ").strip()

    # normalize case so 'Level' counts as palindrome too
    normalized = word.lower()

    if normalized == normalized[::-1]:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

    # Ask if the user wants to check another word
    again = input("Do you want to check another word? (yes/no): ").strip().lower()
    if again != 'yes':
        break