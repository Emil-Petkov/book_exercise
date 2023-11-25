test_file = open('C:\\Users\\emili\\test.txt')
text = test_file.read()  # read file
print(text)

#########################################

test_file = open('C:\\Users\\emili\\test.txt', 'w')
test_file.write('hello, world')  # write in file
test_file.close()  # close file

#########################################
