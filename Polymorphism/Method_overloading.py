'''
Method Overloading:-Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note:- Python does not support method overloading. We may overload the methods but can only use the latest defined method. 


'''

class A():
    def display(self):
        print("Hello")
class B(A):
    def add(self,a=0,b=0,c=0):
        print("Addition of the number is:",a+b+c)

obj=B()
obj.display()
obj.add()
obj.add(20,30)
obj.add(200,300,100)    