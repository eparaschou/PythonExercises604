# write a function that returns the sum of three numbers

import math

NAME = "Elina" # use all caps to define a constant

def sum_of_three_numbers(num1, num2, num3):

    return math.fsum([num1, num2, num3])


#write a function that takes a number and returns its cube

def get_number(number):
    return math.pow(number, 3)


# write a function that takes a name (a string) and returns "Hello <name>"
def get_name(name):
    return f"Hello {name}"

# define a class: student: attributes Fname, Lname, Major. Getter and setter methods
# def a function in this module - call it sum_of_list(list)
# returns the sum
class Student:
    def __init__(self, fname, lname, major):
        self._fname = fname
        self._lname = lname
        self._major = major
    def fname(self):
        return self._fname
    def lname(self):
        return self._lname
    def major(self):
        return self._major
