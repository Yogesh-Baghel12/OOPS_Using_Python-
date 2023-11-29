'''     we do Abstraction when action is same but implementation is different.
ABSTRACTION :- It is a process of hidding the implementation details from the user, only  showing essential details to the user. 
      _________    ___________     ____________
     |first.py |  |second.py  |   |  main.py   | 
     | add()   |->| sub()     |-> |  add()     |
     |_________|  |___________|   |  sub()     |
                                  |____________|


'''
   
   
   
'''import second,first

first.Add()
second.Sub()
'''
#Another moethod using abstract class
'''
1. Object can't be created for abstract class. 
2. object can be created for concrete class. 
3. Decorator: It allow programmer to modify the behaviour of a function or class, whithout permanently modifying. Syntax:-@name
'''


from abc import ABC,abstractmethod

class Car(ABC):  #Abstract Class : Which have abstract method. 
    def show(self):
        print("Every car has a 4 wheels")
    @abstractmethod   #Abstract Method: Method with declaration but not the defination. 
    def Speed(self):
        pass
class Maruti(Car):    #Concrete Class
    def Speed(self):
        print("Speed is 100km/h")
class Suzuki(Car):    #Concrete Class: Class which doesn't have any abstract method. 
    def Speed(self):
        print("Speed is 70km/h")
obj=Maruti()
obj.show()
obj.Speed()
obj2=Suzuki()
obj2.show()
obj2.Speed()