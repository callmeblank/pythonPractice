import re

email = input("email: ").strip()
print(email)
if re.search(r"^[^@\s]+@[^@ ]+\.com$", email):
    print("valid")
else:
    print("invalid")