print(bool(0))  # False
print(bool(1))  # True
print(bool(0.001))  # True
print(bool(-500))  # True

########################

print(bool(None))  # False
print(bool(''))  # False
print(bool(' '))  # True
print(bool('abc'))  # True

#########################

my_list = []
print(bool(my_list))  # False

my_list2 = ['P', 'y', 't', 'h', 'o', 'n']
print(bool(my_list2))  # True

##########################

year = input('Your year of birth is: ')

if not bool(year):
    print('Enter your year of birth.')

# empty value == False
