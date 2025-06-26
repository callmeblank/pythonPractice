class WW:
    #this is not exactly constructor because it follows constructor named __new__
    #and object is created when __new__ is done. so it may be too late to return none in __init
    def __init__(self, name, house="Gryffindor", spell = None): #init for initialize
        #Those lines do not work
        #if not name:
        #   return None
        #raise keyword is very likely throw in java
        if not name:
            raise ValueError("missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.spell = spell
        #overloaded method
    def __str__(self):
        return f"{self.name} from {self.house}\n{self.name}'s spell is {self.spell}"
    
    #This function is called method
    def charm(self):
        match self.spell:
            case "Stag":
                print("🌵")
            case "Otter":
                print("📷 ")
            case "Jacole":
                print("🛩 ")
        
def main():
    ww = get_ww()
    ww.charm()
    print(ww)

def get_ww():
    name = input("WW's name? ")
    house = input("WW's house? ")
    spell = input("WW's spell? ")
    if (not house):
        return WW(name=name, spell=spell)
    return WW(name, house, spell)
if __name__ == "__main__":
    main()