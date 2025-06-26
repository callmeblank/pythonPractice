class WW:
    def __init__(self, name, house): #Default constructor
        self.name = name
        self.house = house
def main():
    ww = get_ww()
    print(f"Name == {ww.name}\nHouse == {ww.house}")

def get_ww():
    name = input("WW's name? ")
    house = input("WW's house? ")
    return WW(name, house)
if __name__ == "__main__":
    main()