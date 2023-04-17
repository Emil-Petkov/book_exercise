numbers = int(input("Enter numbers: "))  # 123456789

while numbers:
    last_number = numbers % 10  # take last digit
    print(f"|{last_number}|", end='')  # result: |9||8||7||6||5||4||3||2||1|

    numbers //= 10  # remove last digit

    

    
