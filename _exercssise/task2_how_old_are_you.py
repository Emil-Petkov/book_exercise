import datetime

current_year = datetime.datetime.now().year

born_date = int(input("What year were you born?\n>>> "))

result = current_year - born_date

print(f"\nYou are {result} years old.")
