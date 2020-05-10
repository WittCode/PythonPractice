'''
This program practices with parent and child classes in python.
This also practices with *args.
'''

class Person:

    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        arg_num = 0
        for arg in args:
            print("arg[" + str(arg_num) + "] " + str(arg))
            arg_num += 1

    def print_info(self):
        print("My name is " + self.name + " and I am " + str(self.age) + " years old.")


class Employee(Person): #Person is the parent class, Employee is the child class.

    def __init__(self, salary, name, age):
        self.salary = salary
        Person.__init__(self, name, age)    #Calls the constructor of the parent class.

    def print_info(self):
        return super().print_info()     #Calls the print info from the parent class.


'''
START OF PROGRAM
'''
employee1 = Employee(50000, "Tom", 24)
employee1.print_info()
