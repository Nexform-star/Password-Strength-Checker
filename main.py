import string

pas = input("Please enter a password: ")
pass_len = len(pas)
if pass_len > 11:
    print("Your password is strong!")
else:
    print("Your password is too short.")

if any(char.isdigit() for char in pas):
    print("Password contains a digit.")
else:
    print("Your password needs at least one digit.")

majuscule = any(char.isupper() for char in pas)
if majuscule == False:
    print("Please include at least one uppercase letter.")
else:
    print("Password contains an uppercase letter.")

minuscule = any(char.islower() for char in pas)
if minuscule == False:
    print("Please include at least one lowercase letter.")
else:
    print("Password contains a lowercase letter.")

ponctuation = any(string.punctuation)
if ponctuation == False:
    print("Your password needs a special character.")
else:
    print("Password contains a special character!")