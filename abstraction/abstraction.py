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


from abc import ABC,abstractmethod

class Car(ABC):
    def show(self):
        print("Every car has a 4 wheels")
    @abstractmethod
    def Speed(self):
        pass
class Maruti(Car):
    def Speed(self):
        print("Speed is 100km/h")
class Suzuki(Car):
    def Speed(self):
        print("Speed is 70km/h")
obj=Maruti()
obj.show()
obj.Speed()
obj2=Suzuki()
obj2.show()
obj2.Speed()