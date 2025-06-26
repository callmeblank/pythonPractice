import csv
characters = []
stop = False
flag = 0

# Get input from user
while (not stop):
    name = input("What's your name? ")
    kind = input("What's your kind? ")
    
    characters.append({"name" : name, "kind" : kind})
    
    flag = input("Continue? (Y or N): ")
    
    valid = False
    while (not valid):
        if (flag.lower() == 'n'):
            valid = True
            stop = True
            print("Out of program")
        elif (flag.lower() == 'y'):
            valid = True
        elif (flag.lower() != 'y'):
            print("not valid")
            flag = input("Continue? (Y or N)")

#write data you get to a file
with open("characters.txt", mode="a", newline="") as cfile:
    writer = csv.DictWriter(cfile, fieldnames=["name", "kind"])
    for character in characters:
        writer.writerow(character)
    
