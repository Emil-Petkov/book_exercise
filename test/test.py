a = [1, 2, 3, 4, 5]
# b = [num * 3 if num % 2 == 0 else num * 2 for num in a]
# print(b)

# list = []
# while a:
#     if a[0] % 2 == 0:
#         list.append(a[0] * 3)
#         del a[0]
#     else:
#         list.append(a[0] * 2)
#         a.remove(a[0])
# print(list)
######################################################################


# ternary_operator#
number = 7  # int(input("Enter a number: "))

result = "even number" if number % 2 == 0 else "odd number"
# If there are square brackets [ ] it will be on a list comprehension

print(result)
