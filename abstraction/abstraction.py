'''     we do Abstraction when action is same but implementation is different.
ABSTRACTION :- It is a process of hidding the implementation details from the user, only  showing essential details to the user. 
      _________    ___________     ____________
     |first.py |  |second.py  |   |  main.py   | 
     | add()   |->| sub()     |-> |  add()     |
     |_________|  |___________|   |  sub()     |
                                  |____________|


'''
   
   
   
import second,first

first.Add()
second.Sub()

#Another moethod using abstract class


