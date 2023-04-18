first_list = [1, 2, 3, 4]
second_list = [1, 2, 3, 4]

for el in first_list:
    if el in second_list:
        continue
    else:
        print("error")
        exit()

print("Тhe lists are the same in length and elements")