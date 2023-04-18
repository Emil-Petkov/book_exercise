# colors = ["White", "Green", "Red"]
#
# for el in colors:
#     print(el, end=" ")  # White Green Red
#
# ########################################################################
#
# for s in colors:
#     print(s, "->", len(s), end=" ")  # White -> 5 Green -> 5 Red -> 3
#
##########################################################################

num = int(input("Enter Fibonacci sequence: "))

a, b = 1, 1

for _ in range(num):
    print(a, end=", ")
    result = a, b = b, a + b

