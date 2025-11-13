# Parent Class
class Animal:
    def speak(self):
        print("The animal speaks") 

# Child Class Dog inheriting from Animal
class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

d=Dog()
c=Cat()
d.speak()  
c.speak()