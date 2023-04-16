txt = list("Hello, world!")
print(txt)
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']

##############################################################################
print(len(txt))
# 13

##############################################################################
print(txt[7])
# w
print(txt[-3])
# l

##############################################################################
print(txt[3:8 + 1])
# ['l', 'o', ',', ' ', 'w', 'o']

##############################################################################

##############################################################################
numbers = [-4, 7, 1, 0, 5]

print(min(numbers))  # -4
print(max(numbers))  # 7
print(sum(numbers))  # 9
print(sorted(numbers))  # [-4, 0, 1, 5, 7]
print(sorted(numbers, reverse=True))  # [7, 5, 1, 0, -4]
print(sorted(numbers)[::-1])  # [7, 5, 1, 0, -4]
print(list(reversed(numbers)))  # [5, 0, 1, 7, -4]
numbers[3] = "hello"
print(numbers)  # [-4, 7, 1, 'hello', 5]
numbers[1:-2] = ["A", "B"]
print(numbers)  # [-4, 'A', 'B', 'hello', 5]
num = list(range(1, 11))
print(num)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[1:3] = []
print(numbers)  # [-4, 'hello', 5]
del numbers[-1]
print(numbers)  # [-4, 'hello']

