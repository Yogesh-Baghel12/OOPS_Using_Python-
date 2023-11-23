'''
Multilevel inheritance is a type of inheritance in object-oriented programming where a class is derived from another class, and then another class is derived from that derived class. This forms a chain of inheritance with multiple levels.

The Example: BASE CLASS[Grandparent]
                  |
            DERIVED CLASS[Parent]
            BASE CLASS[parent]
                  |
            DERIVED CLASS[child]
'''





class Grandparent():
    def Disp(self):
        print("Grandparents")
class Parent(Grandparent):
    def Show(self):
        print("Parents")
class Child(Parent):
    def Display(self):
        print("Childs")
        
c=Child()
c.Display()
c.Show()
c.Disp()