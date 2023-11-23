'''
Hierarchical inheritance is a type of inheritance in object-oriented programming where multiple classes are derived from a single base class. In this type of inheritance, a single base class serves as the parent for two or more derived classes. Each derived class inherits properties and behaviors from the common base class.

The example are :-                              BASE CLASS[Parent]
                                                     |
                                            _________|______________
                                            |                       |
                                            |                       |
                                        DERIVED CLASS[Child1]     DERIVED CLASS[Child2]
                                                           
'''

class Parent():
    def Show(self):
        print("Parents")
class Child1(Parent):
    def Disp(self):
        print("Child1")
class Child2(Parent):
    def Display(self):
        print("Child2")

c=Child1()
c1=Child2()
c.Show()
c1.Show()