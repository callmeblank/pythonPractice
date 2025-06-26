def main():
    witch = get_witch()
    print(f"Name == {witch["name"]}\nHouse == {witch["house"]}")

def get_witch():
    name = input("Witch's name? ")
    house = input("Witch's house? ")
    return {"name" : name, "house": house} #This line makes this program looks like "OOP" with (tuple, list, dict, etc) as an object (even we can return a dict)
    #return a dict can have an advantage that you don't need to remember the location of keys anymore
if __name__ == "__main__":
    main()