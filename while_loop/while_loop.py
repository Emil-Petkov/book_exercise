num = 10

counter = 0

while counter < num:
    counter += 1

    print(counter)

print("\n")

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
############################################################################

n = input("Enter number: ")

txt = "1"

count = 1

while not str(count) == n:
    count += 1

    txt = txt + " + " + str(count)

print("Sum with eval")
print(txt, '=', eval(txt))
# Enter number: 5
# Sum with eval
# 1 + 2 + 3 + 4 + 5 = 15
############################################################################


