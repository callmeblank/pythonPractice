class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("name can't be whitespace")
        self.name = name
class Student(Wizard): ##class A(something B) means A is descendant of B
    def __init__(self, name, house): 
        super().__init__(name) #super() is a way to refer to Wizard class and super().__init__ is
        #the way to inherit all thing in __init__ of parent class
        self.house= house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense against the Dark art")
    print(wizard.name)
    print(student.name)
    print(professor.name)
if __name__ == "__main__":
    main()