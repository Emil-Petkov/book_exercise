def my_func(txt: str):
    print(txt)


txt = input("Txt: ")  # Hello, Python my name is Emil.

my_func(txt)  # Hello, Python my name is Emil.
my_func("Hello (:")  # Hello (:


#########################################################################
def my_func(first_num: float, second_num: int):
    print(f"{first_num / second_num:.2f}")


my_func(11.4, 3)  # 3.80
my_func(4.1, 32)  # 0.13
my_func(0.1, 4)  # 0.03


#########################################################################
def show_elements_in_txt(txt):
    return sorted(list(txt), reverse=True)  # create a list of elements ## Sorted and reverse list


user_input = input("Enter txt: ")  # Python
print(show_elements_in_txt(user_input))  # ['y', 't', 'o', 'n', 'h', 'P']


#########################################################################
def sqsum(n_numbers: int):
    square_of_numbers = [num * num for num in range(1, n_numbers + 1)]
    print(square_of_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]


n = int(input("n numbers: "))  # 17
sqsum(n)
