'''
Inheritance :Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class, called a derived or subclass, to inherit properties and behaviors from an existing class, known as the base or parent class. The idea behind inheritance is to promote code reuse and establish a relationship between classes that reflects an "is-a" relationship.

'''

class Parent():
    def display(self):
        print("Parents")
class child(Parent):
    def Show(self):
        print("Child")
c=child()
c.display()
c.Show()