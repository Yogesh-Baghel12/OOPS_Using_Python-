'''
  Overriding Polymorphism :- Method overriding is an example of run time polymorphism. In this, the specific implementation of the method that is already provided by the parent class is provided by the child class. It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding. In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods.
  
'''

class father():
    def disp(self):
        print("Father")
class son(father):
    def display(self):
        print("Son")
        
c=son()
c.disp()
c.display()