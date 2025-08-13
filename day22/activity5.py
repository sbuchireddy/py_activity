from abc import ABC, abstractmethod

#Abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

#Dog class implementing Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

#Cat class implementing Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())


