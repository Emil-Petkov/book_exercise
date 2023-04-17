def second_max_number(numbers):
    sort = sorted(numbers)
    del sort[-1]
    print(max(sort))


numbers = [77, 2, -99, 27, 3, 1, 18, 31, -4, 15]
second_max_number(numbers)  # 31
