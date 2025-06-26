import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        return f"{name} is in {random.choice(cls.houses)}"

def main():
    harry_house = Hat.sort("Harry")
    print(harry_house)

if __name__ == "__main__":
    main()
        