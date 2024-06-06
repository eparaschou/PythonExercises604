a = 10
b = 13
c = 8

#check if a is greater than b and if is greater print the value of a
if(a>b):
    print(a)
else:
    print(b)

# bool() is used to return or convert value to boolean
x = 5
y = 10
print(bool(x==y))

# exercise 1
#var1 = input("Enter the 1st number: ")
#var2 = input("Enter the 2nd number: ")
#if var1 > var2:
#    print("var1 is greater than var2")

# Ex2: If the number is even square it
num1 = 10
if num1 % 2 ==0:
    print(num1**2)

# Ex3: Check if a number is divisible by 7, if not print its value, else square it
num2 = int(input("enter a number: "))
if num2 % 7 == 0:
    print("It is divisible by 7")
if num2 % 7 != 0:
    print(num2)
else:
    print(num2**2)

number1 = int(input("Enter a number: "))
if number1 % 2 == 0:
    print(f"{number1} is even")
else:
    print(f"{number1} is odd")

#Ex 4
# pass -> passes control to the next line of code
num = 15
if num > 10:
    print("Number is greater than 10")
    pass  # Do nothing and continue
else:
    print("Number is less than or equal to 10")

# elif examples
# Ex5: assume the days of week are 0,1,2,3,4,5,6 from Sunday to Saturday

weekday = int(input("Enter day of the week: "))
if weekday == 0:
    print("Sunday")
elif weekday == 1:
    print("Monday")
elif weekday == 2:
    print("Tuesday")
elif weekday == 3:
    print("Wednesday")
elif weekday == 4:
    print("Thursday")
elif weekday == 5:
    print("Friday")
elif weekday == 6:
    print("Saturday")
else:
    print("Invalid Input")

# Ex6: write a program to find the greatest of three numbers using if-else statements
numb1 = int(input("Enter number 1: "))
numb2 = int(input("Enter number 2: "))
numb3 = int(input("Enter number 3: "))

if numb1 > numb2 and numb1 > numb3:
    print("Numb1 is the greatest number")
elif numb2 > numb1 and numb2 > numb3:
    print("Numb2 is the greatest number")
elif numb3 > numb1 and numb3 > numb2:
    print("Numb3 is the greatest number")
else:
    print("Two or more numbers are equal")

# Ex6 alternative solution
a = 3
b = 1
if a>b:
    if a>c:
        print(a)
    if b>a:
        if b>c:
            print(b)
    else:
        print(c)

numb1 = int(input("Enter number 1: "))
numb2 = int(input("Enter number 2: "))
numb3 = int(input("Enter number 3: "))
numb4 = int(input("Enter number 4: "))

if numb1 > numb2 and numb1 > numb3 and numb1 > numb4:
    print("Number 1 is the greatest number")
elif numb2 > numb1 and numb2 > numb3 and numb2 > numb4:
    print("Number 2 is the greatest number")
elif numb3 > numb1 and numb3 > numb2 and numb3 > numb4:
    print("Number 3 is the greatest number")
else:
    print("Number 4 is the greatest")

# Ex7 Use OR operator to find if the number is divisible by 5 or 7 then print your are a winner
# If the number is also a multiple of 8 print you a super winner
number = int(input("Enter a number: "))
if number % 5 == 0 or number % 7 == 0:
    print("You are a winner")
    if number % 8 == 0:
        print("You are a super winner")
else:
    print("Better luck next time")

number=int(input("What is your number? "))
if(number%5==0 or number%7==0):
    if(number%8==0):
        print("You are a super winner!")
    else:
        print("You are a winner!")
else:
    print("better luck next time :(")