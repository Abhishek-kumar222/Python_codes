# Create a class Pets from a class Animal, and further create a class Dog from class Pets, and add a method bark to class Dog.

class Animals:
  pass

class Pets(Animals):
  pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("the dog is barking")

o = Dog()
o.bark()

   