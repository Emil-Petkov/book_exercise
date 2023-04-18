user_numbers = [2, 4, 5]  # list(map(int, input().split(",")))
upper_limit = 10  # int(input("Enter upper limit of natural numbers: "))

filter = user_numbers

sum_of_numbers = 0

for i in range(1, upper_limit + 1):
    if not i in filter:
        sum_of_numbers += i
    else:
        continue

print("Sum: ", sum_of_numbers)
