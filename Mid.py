# MCQ
new_list = ['python', 'development']
new_list.append('in progress')
print(new_list)

# MCQ 2
value = 11 // 2
print(value)

# Write a Python program to create a list those numbers which are divisible by 7 and 9, between 1400 and 2000 (both included).
list1 = []
for num in range(1400,2001):
    if num % 7 == 0 and num % 9 == 0:
        list1.append(num)
print(list1)

# Write a program to print the multiplication table of a number. Print the values from 1 to 10. Use the input statement to accept the number from the user.
num = int(input("Enter a number: "))
for i in range(1,11):
    multiplication = num * i
    print(f'{num} x {i} = {multiplication}')

#Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).

def day_name(day):
    if day in range(0,7):
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][day]
    return None

day_number = int(input("Enter day number: "))
selected_day = day_name(day_number)
print(selected_day)

# Write a Python function to calculate
# the factorial of a number  if the number is an even number (a non-negative integer)
# cube of the number if it is odd.
# The function accepts the number as an argument.

def factorial(number):
    if number % 2 == 0:
        fact = 1
        for i in range(1, number+1):
            fact *= i
        return fact
    else:
        return number ** 3
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial for the number {number} is: {result}")

# A prime number is an integer that can only be divided by itself and by 1 (it cannot be divided by any other numbers).
# Write a program to create a list of prime numbers between 2 and 100, both included.

list1 = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        list1.append(num)
print(f'The prime numbers between 2 and 100 are: {list1}')



# Write code to create a list of the first 10 even numbered elements in the Fibonacci series.
fib_list = []
a,b = 1,1
while len(fib_list) < 10:
    if b % 2 == 0:
        fib_list.append(b)
    a,b = b, a+b
print(f'First 10 even Fibonacci numbers: {fib_list}')


# Create a function that takes 3 arguments - 2 numbers (integers or floats) and one of the following six arithmetic operators (as a string): +, -, /, *, //, %.
# The function calculates the value of the operation on the two numbers and returns that value.
# Show test code for at least 3 operations using both integers and floats.

def calculate_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2
    elif operator == '//':
        return num1 // num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Try again"
print(calculate_operation(2.4, 4, '*'))
print(calculate_operation(10, 3, '%'))
print(calculate_operation(12.5, 5, '/'))
print(calculate_operation(12.5, 4, '//'))

# how many times the loop runs
# 7
number = 70
guess = 55
while number != guess:
    if number > guess:
        guess = guess + 10
    else:
        guess = guess - 1
print('The number is:', guess)

