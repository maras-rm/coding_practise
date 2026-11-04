# Challenges from: https://www.w3schools.com/python/python_challenges.asp   - Specifically from classes onwards

# Challenge 1: Classes/Objects :
# - OOP - objects that have properties and methods.
# Create a class called Person
# Add an __init__ method that takes name and age as parameters
# Add a method called greet that prints "Hello, my name is " followed by the name
# Create an object p1 of the class with name "John" and age 36
# Call the greet method on p1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

# Challenge 2: __init__ Method:
# - assigning values to object properties - or perform operations when objects are created.
# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says Woof!")

# Challenge 3: class properties:
# - properties are variables belonging to a class.
# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Challenge 4: Inheritance
# - Inheriting properties and methods from other classes.
# Create a parent class Animal with an __init__ that takes name
# Add a method speak that prints the name
# Create a child class Bird that inherits from Animal
# Create an object b1 = Bird("Rex")
# Call b1.speak()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)

class Bird(Animal):
    pass


# Challenge 5: Polymorphism
# - Having multiple classes with same named methods.
# Create a class Cat with a method sound that prints "Meow"
# Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
# Create objects c1 = Cat() and f1 = Fox()
# Call sound() on both objects

class Cat:
    def sound(self):
        print("Meow")

class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")  


# Challenge 6 : Encapsulation
# - protecting data and how it is accessed.
# Create a class ScoreBoard
# Add an __init__ with a score parameter and store it as a private attribute
# Add a method called get_score that returns the private score
# Create an object sco1 with a score of 0
# Print the score of sco1  

class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return(self.__score)


if __name__ == "__main__":
    # For challenge 1
    p1 = Person("John", 36)
    p1.greet()

    # For challenge 2
    d1 = Dog("Buddy", 3)
    d1.bark()

    # For challenge 3
    s1 = Student("Anna", "A")
    print(s1.grade)
    s1.grade = "B"
    print(s1.grade)

    # For challenge 4:
    b1 = Bird("Rex")
    b1.speak()

    # For challenge 5:
    c1 = Cat()
    f1 = Fox()

    c1.sound()
    f1.sound()

    # For challenge 6:
    sco1 = ScoreBoard(0)
    print(sco1.get_score())