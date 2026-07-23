import string

password = input("Enter the password to evaluate: ")

score = 0

if len(password) >= 8:
    score += 1

has_digit = any(char.isdigit() for char in password)
if has_digit:
    score += 1

has_upper = any(char.isupper() for char in password)
if has_upper:
    score += 1

has_symbol = any(char in string.punctuation for char in password)
if has_symbol:
    score += 1

if score <= 2:
    print("Result: Weak Password")
elif score == 3:
    print("Result: Medium Password")
else:
    print("Result: Strong Password")