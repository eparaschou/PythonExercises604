# _init_() -> assigns values to object properties when object is being created
# _str_() -> controls what should be returned when the class object is represented as a string
# name of a class begins with a capital
# an object is mutable
class Automobile:
    windshield = ""
    tires = ""
    headlights = ""

automobile1 = Automobile()

automobile1.tires = "4 tires"
automobile1.headlights = "2 headlights"
automobile1.windshield = "black windshield"
print("The automobile has:","\n", automobile1.windshield,"\n", automobile1.headlights,"\n",automobile1.tires)

class Student:
    def __init__(self, name, dob, id, major, gpa=0):
        self.name = name
        self.dob = dob
        self.id = id
        self.major = major

# main program
# create an instance (object) of this class
student1 = Student('Elina','2/25/2000','AU123','analytics')
student1.gpa = 3.9
print(student1.name, student1.dob,student1.gpa)
student1.name = 'Rob'
print(student1.name)
