def sum_odd_numbers(numbers):
    sum = 0

    for i in numbers:
        if not i % 2 == 0:
            sum += abs(i)

    print(f"Sum of odd numbers is: {sum}")


numbers = [77, 2, -99, 27, 3, 1, 18, 31, -4, 15]
print("Numbers: [77, 2, -99, 27, 3, 1, 18, 31, -4, 15]")
sum_odd_numbers(numbers)  # 253
