class WW:
    #this is not exactly constructor because it follows constructor named __new__
    #and object is created when __new__ is done. so it may be too late to return none in __init
    def __init__(self, name, house): #init for initialize
        #Those lines do not work
        #if not name:
        #   return None
        #raise keyword is very likely throw in java
        if not name:
            raise ValueError("missing name")
        if house not in ["Griffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid house")
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