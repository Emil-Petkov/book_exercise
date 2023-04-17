from math import factorial

number = int(input("Enter factorial: "))

if number > 0:

    result = factorial(number)
    print(f"Factorial of {number} = {result}")
else:
    print("This is negative number")

####################################################################
# factorial = 1
#
# for i in range(1, number + 1):
#     factorial *= i
#
# print(f"\nFactorial of {number} = {factorial}")
