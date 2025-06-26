def main():
    witch = get_witch()
    print(f"Name == {witch[0]}\nHouse == {witch[1]}")

def get_witch():
    return [input("Witch's name? "), input("Witch's house? ")] #This line makes this program looks like "OOP" with (tuple, list, dict, etc) as an object (even we can return a dict)

if __name__ == "__main__":
    main()