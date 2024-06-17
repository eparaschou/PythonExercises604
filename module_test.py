import myimportmodule

var1 = 10
var2 = 2
var3 =45

total = myimportmodule.sum_of_three_numbers(var1,var2,var3)
print("Sum of three numbers is:", total)

num1 = 3
print(myimportmodule.get_number(num1))

name1 = "Sofia"
print(myimportmodule.get_name(name1))

print("Hello this is", myimportmodule.NAME)

student1 = myimportmodule.Student("Mary","Paris","Analytics")
print(student1.fname())
