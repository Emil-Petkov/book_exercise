def kilometers(miles: float):
    print("Info: One mile equal 1.609344 kilometers.\n")
    km = miles * 1.609344
    print(f"{miles} miles = {km:.2f} kilometers.")


miles = float(input("Enter miles: "))
kilometers(miles)
