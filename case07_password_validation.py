password = input("Enter password: ")

errors = []

if len(password) < 8:
    errors.append("At least 8 characters required")

if not any(ch.isupper() for ch in password):
    errors.append("At least one uppercase letter required")

if not any(ch.islower() for ch in password):
    errors.append("At least one lowercase letter required")

if not any(ch.isdigit() for ch in password):
    errors.append("At least one digit required")

if len(errors) == 0:
    print("Password is valid")
else:
    print("Password is invalid")
    for error in errors:
        print("-", error)
