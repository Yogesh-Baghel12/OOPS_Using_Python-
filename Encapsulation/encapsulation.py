'''
ENCAPSULATION :- Wrapping of DATA & Function into a single entity. 
  
Private variable :To accomplish this in Python, just follow the convention by prefixing the name of the variable by a single underscore “_”.
public variable : to accomplish this in python , just follw the convention normally like other variable declare like that only.
  

'''


class Public():
    a=10 
    def disp(self):
        print("Welcome")
class Private():
   __a=20 
   def display(self):
       print("Welcome")
       print(self.__a)#use to access the private variable.
       
obj1=Public()
print(obj1.a)
#if we want to access private variable like public variable it give the error: error is Private object has no attribute 'a'.
obj2=Private()
#print(obj2.a)

#we can access the private variable like that by printing the private variable inside the fuction of that class. 
print(obj2.display())