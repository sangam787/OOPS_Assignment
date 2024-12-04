

"OOPS ASSIGNMENT QUESTIONS AND ANSWERS"

"1. What are the five key concepts of Object-Oriented Programming (OOP)?" 
"""
The five key concepts of Object-Oriented Programming(OOP) are :
(1)- Classes and Objects
A class is a blueprint for creating objects, which are instances of the class. 
A class defines the properties and behaviors of its objects

(2)- Inheritance
This mechanism allows classes to inherit properties and behaviors from parent classes.

(3)- Polymorphism
This principle allows objects to take on multiple forms, meaning the same object 
can behave differently depending on the context.

(4)- Encapsulation
This concept involves hiding an object's internal details and only exposing the necessary information.

(5)- Abstraction
This is a way to simplify complex reality by modeling classes on essential properties and behaviors. 

"""

"""
Que-2. Write a Python class for a 'Car with attributes for 'make', 'model', 
and 'year'. Include a method to display the car's information. 
"""

"defining a class named 'Car'"
# class Car():
#     def __init__(self, name , model, year):
#         self.name = name
#         self.model = model
#         self.year = year
   
#     def car_information(self):
#         print("The name of car  is {}".format(self.name))
#         print("model number is {}".format(self.model))
#         print("year is {}".format(self.year))    
    
        
# car1 = Car("ford", "ABCXX", 2024)
# print(car1.car_information())


"""

3. Explain the difference between instance methods and class methods. 
Provide an example of each. 


(1)-Instance Methods in Python:-


Instance methods are the most common type of methods in Python classes. 
They are associated with instances of a class and operate on the instance's data. 
When defining an instance method, the method's first parameter is typically named self, 
which refers to the instance calling the method. This allows the method to access 
and manipulate the instance's attributes.
for example-
"""
# class Student:
#     def __init__(self, name, institute):
#         self.name = name
#         self.institute = institute

#     def introduce(self):
#         return f"Hi, I'm {self.name} and I study in {self.institute}."


# # Creating an instance of the class
# stu1 = Student("Sangam", "PWskills")

# # Calling the instance method
# print(stu1.introduce())  

"""
(2)-Class Method in Python:-

Class methods are associated with the class rather than instances. 
They are defined using the @classmethod decorator and take the class itself 
as the first parameter, usually named cls. Class methods are useful for tasks 
that involve the class rather than the instance, such as creating class-specific 
behaviors or modifying class-level attributes.
for example-
"""
# class MyClass:
#     class_variable = 0

#     def __init__(self, value):
#         self.instance_variable = value

#     @classmethod
#     def class_method(cls, x):
#         cls.class_variable += x
#         return cls.class_variable

# # Creating instances of the class
# obj1 = MyClass(5)
# obj2 = MyClass(10)

# # Calling the class method
# print(MyClass.class_method(3))  # Output: 3
# print(MyClass.class_method(7))  # Output: 10





"""
4. How does Python implement method overloading? Give an example. 
Method Overloading:

Two or more methods have the same name but different numbers of 
parameters or different types of parameters, or both. These methods are 
called overloaded methods and this is called method overloading. 
The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. 
for example
"""
# First product method.
# Takes two argument and print their
# product


# def product(a, b):
#     p = a * b
#     print(p)

# Second product method
# Takes three argument and print their
# product


# def product(a, b, c):
#     p = a * b*c
#     print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
# product(4, 5, 5)

"""
Que-5. What are the three types of access modifiers in Python? How are they denoted? 

Answer:-
A Class in Python has three types of access modifiers:

(1)Public Access Modifier: Theoretically, public methods and fields can be accessed directly by any class.
class Geek:
"""
# class Pwskills:  
   
#     # constructor
#     def __init__(self, name, age):

#         # public data members
#         self.Name = name
#         self.Age = age

#     # public member function
#     def displayAge(self):

#         # accessing public data member
#         print("Age: ", self.Age)


# # creating object of the class
# obj = Pwskills("Sangam", 25)

# # finding all the fields and methods which are present inside obj
# print("List of fields and methods inside obj:", dir(obj))

# # accessing public data member
# print("Name:", obj.Name)

# # calling public member function of the class
# obj.displayAge()


"(2)Protected Access Modifier: Theoretically, protected methods and fields can be accessed within the same" 
# class it is declared and its subclass.
# class  Student:

#     # protected data members
#     _name = None
#     _roll = None
#     _branch = None

#     # constructor
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch

#     # protected member function
#     def _displayRollAndBranch(self):

#         # accessing protected data members
#         print("Roll:", self._roll)
#         print("Branch:", self._branch)
# # Pwskills(Student):

#     # constructor
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)

#     # public member function
#     def displayDetails(self):

#               # accessing protected data members of super class
#         print("Name:", self._name)

#         # accessing protected member functions of super class
#         self._displayRollAndBranch()


# stu = Student("Sangam", 1234567, "Computer Science")
# print(dir(stu))

# # protected members and methods can be still accessed
# print(stu._name)
# stu._displayRollAndBranch()

# # Throws error
# # print(stu.name)
# # stu.displayRollAndBranch()

# # creating objects of the derived class
# obj = Pwskills("Subham", 1706256, "Information Technology")
# print("")
# print(dir(obj))

# # calling public member functions of the class
# obj.displayDetails()

"(3)Private Access Modifier: Theoretically, private methods and fields can be only accessed within the same class it is declared."
# class Geek:

#     # private members
#     __name = None
#     __roll = None
#     __branch = None

#     # constructor
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch

#     # private member function
#     def __displayDetails(self):

#         # accessing private data members
#         print("Name:", self.__name)
#         print("Roll:", self.__roll)
#         print("Branch:", self.__branch)

#     # public member function
#     def accessPrivateFunction(self):

#         # accessing private member function
#         self.__displayDetails()

# # creating object
# obj = Geek("R2J", 1706256, "Information Technology")

# print(dir(obj))
# print("")

# # Throws error
# # obj.__name
# # obj.__roll
# # obj.__branch
# # obj.__displayDetails()

# # To access private members of a class
# print(obj._Geek__name)
# print(obj._Geek__roll)
# print(obj._Geek__branch)
# obj._Geek__displayDetails()

# print("")

# # calling public member function of the class
# obj.accessPrivateFunction()





"""
6. Describe the five types of inheritance in Python. Provide a simple 
example of multiple inheritance.

Inheritance is defined as the mechanism of inheriting the properties of the base class to the child class.
There are five types of inheritance in Python.

(1)- Single Inheritance:- Single inheritance enables a derived class to inherit properties from a 
single parent class, thus enabling code reusability and the addition of new features to existing code.
"""
"""
(2)- Multiple Inheritance:- When a class can be derived from more than one base class this type of inheritance 
is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited 
into the derived class. 
"""
#     #Base class 1
# class Mother:
#     mothername = ""
#     def mother(self):
#         print(self.mothername)
#      # Base class 2
# class Father:
#     fathername = ""
#     def father(self):
#         print(self.fathername)
#      # Derived class
# class Son(Mother, Father):
#     def Parents(self):
#         print("Father :", self.fathername)
#         print("mother :", self.mothername)

# S1 = Son()
# S1.fathername = "Ram"
# S1.mothername = "Sita"
# S1.Parents()

"""
(3)- Multilevel Inheritance:- In multilevel inheritance, features of the base class and the derived class 
are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather. 

(4)- Hierarchical Inheritance:- When more than one derived class are created from a single base this type of 
inheritance is called hierarchical inheritance.



"(5)- Hybrid Inheritance:- Inheritance consisting of multiple types of inheritance is called hybrid inheritance."




"""
"""
7. What is the Method Resolution Order (MRO) in Python? How can you 
retrieve it programmatically?

Method resolution order:
In Python, every class whether built-in or user-defined is derived from the object class and all the objects 
are instances of the class object. Hence, the object class is the base class for all the other classes.
In the case of multiple inheritance, a given attribute is first searched in the current class if it's not found 
then it's searched in the parent classes. The parent classes are searched in a left-right fashion and each 
class is searched once.
The order that is followed is known as a linearization of the class Derived and this order is found out using 
a set of rules called Method Resolution Order (MRO).
To view the MRO of a class: 
 

Use the mro() method, it returns a list 
Eg. Class4.mro()
Use the _mro_ attribute, it returns a tuple 
Eg. Class4.__mro__ 
"""
# Python program to demonstrate
# super()

# class Class1:
# 	def m(self):
# 		print("In Class1")

# class Class2(Class1):
# 	def m(self):
# 		print("In Class2")
# 		super().m()

# class Class3(Class1):
# 	def m(self):
# 		print("In Class3")
# 		super().m()

# class Class4(Class2, Class3):
# 	def m(self):
# 		print("In Class4") 
# 		super().m()
	
# print(Class4.mro())		 #This will print list
# print(Class4.__mro__)	 #This will print tuple







"""
8. Create an abstract base class 'Shape' with an abstract method area(). 
Then create two subclasses "Circle' and 'Rectangle that implement the 'area() method. 
"""
# define a function for calculating
# the area of a shapes
# def calculate_area(name):
#     # name = name.lower()

# # converting all characters
# # into lower cases
     

# # check for the conditions
# 	if name == "rectangle":
# 		l = int(input("Enter rectangle's length: "))
# 		b = int(input("Enter rectangle's breadth: "))
	
# 	# calculate area of rectangle
# 		rect_area = l * b
# 		print(f"The area of rectangle is {rect_area}.")

	
# 	elif name == "circle":
# 		r = int(input("Enter circle's radius length: "))
# 		pi = 3.14
		
# 	# calculate area of circle
# 		circ_area = pi * r * r
# 		print(f"The area of circle is {circ_area}.")
		
	
# 	else:
# 		print("Sorry! This shape is not available")

# # driver code
# if __name__ == "__main__" :

#  print("Calculate Shape Area")
# shape_name = input("Enter the name of shape whose area you want to find: ")

# # function calling
# print(calculate_area("circle"))




"9. Demonstrate polymorphism by creating a function that can work with different shape objects to calculate and print their areas." 

# # define a function for calculating
# # the area of a shapes
# def calculate_area(name):
#     # name = name.lower()

# # converting all characters
# # into lower cases
     

# # check for the conditions
# 	if name == "rectangle":
# 		l = int(input("Enter rectangle's length: "))
# 		b = int(input("Enter rectangle's breadth: "))
	
# 	# calculate area of rectangle
# 		rect_area = l * b
# 		print(f"The area of rectangle is {rect_area}.")

# 	elif name == "square":
# 		s = int(input("Enter square's side length: "))
	
# 	# calculate area of square
# 		sqt_area = s * s
# 		print(f"The area of square is {sqt_area}.")

# 	elif name == "triangle":
# 		h = int(input("Enter triangle's height length: "))
# 		b = int(input("Enter triangle's breadth length: "))
	
# 	# calculate area of triangle
# 		tri_area = 0.5 * b * h
# 		print(f"The area of triangle is {tri_area}.")

# 	elif name == "circle":
# 		r = int(input("Enter circle's radius length: "))
# 		pi = 3.14
		
# 	# calculate area of circle
# 		circ_area = pi * r * r
# 		print(f"The area of circle is {circ_area}.")
		
# 	elif name == 'parallelogram':
# 		b = int(input("Enter parallelogram's base length: "))
# 		h = int(input("Enter parallelogram's height length: "))
	
# 	# calculate area of parallelogram
# 		para_area = b * h
# 		print(f"The area of parallelogram is {para_area}.")
	
# 	else:
# 		print("Sorry! This shape is not available")

# # driver code
# if __name__ == "__main__" :

#  print("Calculate Shape Area")
# shape_name = input("Enter the name of shape whose area you want to find: ")

# # function calling
# print(calculate_area("circle"))

"""
10. Implement encapsulation in a 'BankAccount class with private attributes for 
'balance and account_number'. Include methods for deposit, withdrawal, and balance inquiry. 
"""
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
# class Bank_Account:
# 	def __init__(self):
# 		self.balance=0
# 		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

# 	def deposit(self):
# 		amount=float(input("Enter amount to be Deposited: "))
# 		self.balance += amount
# 		print("\n Amount Deposited:",amount)

# 	def withdraw(self):
# 		amount = float(input("Enter amount to be Withdrawn: "))
# 		if self.balance>=amount:
# 			self.balance-=amount
# 			print("\n You Withdrew:", amount)
# 		else:
# 			print("\n Insufficient balance ")

# 	def display(self):
# 		print("\n Net Available Balance=",self.balance)

# # Driver code

# # creating an object of class
# s = Bank_Account()

# # Calling functions with that class object
# s.deposit()
# s.withdraw()
# s.display()


"""
11. Write a class that overrides the_str_and_add__magic methods. 
What will these methods allow you to do? 
"""



"""
12. Create a decorator that measures and prints the execution time of a function. 
import time
"""
# import time

# def measure_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
#         return result
#     return wrapper

# # Example usage
# @measure_execution_time
# def calculate_multiply(numbers):
#     tot = 1
#     for x in numbers:
#         tot *= x
#     return tot

# # Call the decorated function
# result = calculate_multiply([1, 2, 3, 4, 5])
# print("Result:", result)




"""
13. Explain the concept of the Diamond Problem in multiple inheritance. 
How does Python resolve it? 

The "diamond problem" (also sometimes referred to as the "deadly diamond of death") 
is an ambiguity that arises when a class inherits from two or more classes that have one common superclass.
Python's Solution to the Diamond Problem
Python has a way to address this issue, it uses an approach called Method Resolution Order (MRO), which follows 
the C3 linearization or just "C3 superclass linearization". This algorithm assures that a class always precedes 
its parents and a parent precedes the other parent if it's derived from it. Python also has super() function that 
helps with dynamic dispatching.
"""
# class A:
#     def display(self):
#         print("Display method from class A")

# class B(A):
#     def display(self):
#         print("Display method from class B")

# class C(A):
#     def display(self):
#         print("Display method from class C")

# class D(B, C):
#     pass

# d = D()
# d.display()
# print(D.mro())


"14. Write a class method that keeps track of the number of instances created from a class." 
"""
Instances of a class mean the objects created for a particular class. A single class can have 
multiple objects of it. Here, we will find the count of the number of instances of a class in Python.
"""
# code 
# class Pwskills: 
	
# 	# this is used to print the number 
# 	# of instances of a class 
# 	counter = 0

# 	# constructor of Pwskills class 
# 	def __init__(self): 
		
# 		# increment 
# 		Pwskills.counter += 1


# # object or instance of Pwskills class 
# stu1 = Pwskills() 
# stu2 = Pwskills() 
# stu3 = Pwskills() 
# print(Pwskills.counter) 
