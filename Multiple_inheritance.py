'''
Multiple inheritance is a feature in object-oriented programming where a class can inherit attributes and methods from more than one parent class. In a multiple inheritance scenario, a derived class can inherit from two or more base classes. This allows the derived class to acquire the properties and behaviors of all its parent classes.

The Exapmle are:-                                  BASE CLASS[FATHER]                  BASE CLASS[MOTHER]
                                                        |                                   |  
                                                        |                                   | 
                                                        |___________________________________|
                                                                          |
                                                                          |
                                                                    DERIVED CLASS[Child]



'''





class Father():
    def Disp(self):
        print("Father")
class Mother():
    def Show(self):
        print("Mother")
class Child(Father,Mother):
    def Display(self):
        print("Child")
        
c=Child()
c.Show()
c.Disp()