import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+) ?, ?(.+)$", name): #walrus operator, it just assigns re.search() to matches and use boolean return type
    fname = matches.group(1).strip()
    lname = matches.group(2).strip()
    name = f"{fname} {lname}"
print(name)