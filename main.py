import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*<>?"
length = int(input("Enter length of password: "))
print("Choose character set for password from these:")
print("1. Uppercase")
print("2. Lowercase")
print("3. Digits")
print("4. Special characters")
print("5. Exit")
all_chars = ""
while True:
    choice = int(input("Pick a number: "))
    if choice == 1:
        all_chars += uppercase_letters
    elif choice == 2:
        all_chars += lowercase_letters
    elif choice == 3:
        all_chars += digits
    elif choice == 4:
        all_chars += symbols
    elif choice == 5:
        break
    else:
        print("Please pick a valid option")

password = "".join(random.sample(all_chars, length))
print(password)