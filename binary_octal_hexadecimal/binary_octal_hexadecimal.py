number = 1723

print(bin(number))  # 0b11010111011
print(oct(number))  # 0o3273
print(hex(number))  # 0x6bb
########################################################################################

negative_number = -1703

print(bin(negative_number))  # -0b11010100111
print(oct(negative_number))  # -0o3247
print(hex(negative_number))  # -0x6a7
########################################################################################


return_to_number = "-0b11010100111"
print(int(return_to_number, 2))  # -1703

return_to_number = "-0o3247"
print(int(return_to_number, 8))  # -1703

return_to_number = "-0x6a7"
print(int(return_to_number, 16))  # -1703
