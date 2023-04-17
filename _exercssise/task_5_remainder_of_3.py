list_of_numbers = [num for num in range(0, int(input("Enter number: ")) + 1)]
print()

result = []

for num in list_of_numbers:
    if num % 5 == 3:
        result.append(num)

print(f"Numbers that divide by 5 are equal to 3\n{result}\n")
print(f"Reverse list of the numbers\n{sorted(result, reverse=True)}")
