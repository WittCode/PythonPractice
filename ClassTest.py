'''
This program is used to experiment when the magic (dunder) methods in python are called.
'''


class ClassTest:

    def __init__(self, name):
        print("Created " + name + ".")
        self.salary = 100
        self.name = name

    def __str__(self):
        return "This the string method of class test."

    def __add__(self, other):
        return "The combined salaries are {}.".format(self.salary + other.salary)

    def __del__(self):
        print(self.name + " has been destroyed.")

#Calls the __init__() method.
classTest = ClassTest("Object 1")
classTest2 = ClassTest("Object 2")

#Calls the __str__() method.
print(classTest)

#Calls the __add__() method.
print(classTest + classTest2)

#Calls the __del__() method.
del classTest
del classTest2
