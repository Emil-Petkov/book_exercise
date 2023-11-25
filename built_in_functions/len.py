print(len('simple text'))  # 11

my_list = ['dog', 'cat', 'mouse', ]  # 3
print(len(my_list))

my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', }  # 4
print(len(my_dict))

fruit_list = ['apple', 'orange', 'kiwi', 'watermelon']

for fruit in range(0, len(fruit_list)):
    print(f'Fruit: {fruit} is {fruit_list[fruit]}')

# Fruit: 0 is apple
# Fruit: 1 is orange
# Fruit: 2 is kiwi
# Fruit: 3 is watermelon
