class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Instantiate the Dog object
# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access the instance attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.species)  # Output: Canis familiaris
print(Dog.species)  # Output: Canis familiaris
print(my_dog.name, "is", Dog.species, my_dog.age)

# Call the instance methods
print(my_dog.description())  # Output: Buddy is 3 years old
print(my_dog.speak("Woof"))  # Output: Buddy says Woof

class Animal(Dog):
    def __init__(self, other_name, other_age, other_species):
        super().__init__("Doggy", 5)
        self.other_name = other_name
        self.other_age = other_age
        self.other_species = other_species

    def speak1(self, sound=""):
        return f"{self.other_name} is {self.other_age} years old and says {sound}"
    
    def friends(self):
        return f"{self.other_name} and {self.name} are good friends"
    
my_animal = Animal("Tom", 3, "cat")

print(my_animal.speak("Woof"))
print(my_animal.speak1("Miao"))
print(my_animal.friends())