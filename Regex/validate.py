import re

email = input("email: ").strip()

if re.search(r"^[\w]+@([\w_-]+\.)*[\w_-]+(\.edu|\.com|\.vn|\.gov)$", email): 
    #email has to be formatted as email@(something.)*(something)(.gov or .edu or .com, ...)$
    print("valid")
else:
    print("invalid")