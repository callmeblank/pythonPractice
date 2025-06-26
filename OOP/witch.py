class WW:
    #this is not exactly constructor because it follows constructor named __new__
    #and object is created when __new__ is done. so it may be too late to return none in __init
    def __init__(self, name, house="Gryffindor", spell = None): #init for initialize
        #Those lines do not work if you purpose is stop to initalize it. Because it's initialized at __new__ method (not in __init__)
        #if not name:
        #   return None
        self.name = name 
        self.house = house #self.house is not instance variable. it a setter method defined below
        #and house here serves as parameter for that setter method
        self.spell = spell
        #overloaded method
    def __str__(self):
        return f"{self.name} from {self.house}\n{self.name}'s spell is {self.spell}"
    
    #getter
    @property
    def house(self):
        return self._house #define attribute here instead of __init__
    @property
    def name(self):
        return self._name
    #setter. decorator muse be @<getter-name>.setter
    @name.setter
    def name(self, name):
        #raise keyword is very likely throw in java
        if not name:
            raise ValueError("missing name")
        self._name = name
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("There's no suck house")
        self._house = house    
    #This function is called method
    def charm(self):
        match self.spell:
            case "Stag":
                print("🌵")
            case "Otter":
                print("📷")
            case "Jacole":
                print("🛩")
            case _:
                print("🧮")
        
def main():
    ww = get_ww()
    ww.charm()
    print(ww.name)
    print(ww.house)

def get_ww():
    name = input("WW's name? ")
    house = input("WW's house? ")
    spell = input("WW's spell? ")
    if (not house):
        return WW(name=name, spell=spell)
    return WW(name, house, spell)
if __name__ == "__main__":
    main()