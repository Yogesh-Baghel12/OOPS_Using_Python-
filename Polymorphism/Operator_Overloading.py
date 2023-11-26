'''
Overloading : Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note:- Python does not support method overloading. We may overload the methods but can only use the latest defined method. 

'''


class a():
    def display(self,a,b):
        print("Addition of Two number :",a+b)
class b(a):
    def disp(self,str,str1):
        print("Concatenation of two string:",str+str1)
        
obj=b()
obj.display(10,20)
obj.disp("roh","it")
