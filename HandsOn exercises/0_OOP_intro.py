# Define a class
class Student:
    # Class attribute -> global attribute for the whole class
    university = "Politecnico di Milano"

    # Special method -> initialization of attributes
    def __init__(self, name, age, course):
        self.nome  = name
        self.anni  = age
        self.corso = course

    # Class method
    def describe_me(self): #Print attributes
        print("Name: {}, Age: {}, Course: {}".format(self.nome, self.anni, self.corso))

    # Special method
    def __str__(self) -> str: #Return a string ("-> str"), __str__ -> function called when we use the print()
        return "{} is {} years old and is enrolled in {}".format(self.nome, self.anni, self.corso)

# Instantiate an object of class Student
stud1 = Student("Pedro", 22, "Neuroengineering")

# Call some methods
stud1.describe_me()
print(stud1) # note that the .__str__ method is called with a print function


# Let's create a child class
class LabStudent(Student):

    def __init__(self, name, age, grade, course="LTEB"): #Chil class can use all attributes from parent class + additional attributes and methods
        super().__init__(name, age, course) #Parent class (inheritance)
        self.voto = grade

    def __str__(self): #Redefine / overwrite the method __str__ from parent class, this method is already in the parent class, but here we are overwriting it to a new method
        return "{} is a LTEB student who got {} at the exam".format(self.nome, self.voto) #<-- we can override the parent method and define a new version of it

stud2 = LabStudent("Davide", 27, 30) # note that we don't need to pass the last argument, course, since it is defaulted inside the class definition

stud2.describe_me()
print(stud2)

