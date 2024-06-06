var1 = 10
var2 = 23
totVar = var1 + var2
print(totVar)
bvar = totVar / var1
print(bvar)

# why is bvar a float data type although totVar and var1 are integers?
# / always performs floating-point division, regardless of whether the operands are integers

# which operator can you use so that bvar is an integer instead of a float?
# the floor division operator //

# var2 to the power of 7
print(var2**7)

# find square root of totVar
print(totVar**0.5)

print(9**0.5)

# PEDMAS order 1/2 is not the same as 0.5 make sure to add parenthesis
print(9**(1/2))

# pyramid of numbers
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')

# type in the terminal section
name = input("Enter your name here: ")
print("Enter your name here:",name)

var3 = input("Enter 1st num:")
var4 = input("Enter 2nd num:")
var3 = int(var3)
print(type(var3))
var4 = int(var4)
totVar2 = var3 + var4
print(totVar2)

var5 = input("Enter string1: ")
var6 = input("Enter string2: ")
var7 = 2
# concanates strings ElinaGreek
print(var5+var6)

# repeats it by the number of integer you assigned
print(var5*var7)

#P is the principal
#N is the period
# R is the rate of interest
# A is the amount after the simple interest calculation
# Use input command to accept P,N,R and calculate A

P = int(input("Enter principal:"))
N = int(input("Enter number of periods:"))
R = float(input("Enter rate of interest:"))
A = P * N * R/100
print(A)










