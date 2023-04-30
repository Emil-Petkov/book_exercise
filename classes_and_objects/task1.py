class Hello:
    pass


obj_1 = Hello()
obj_2 = Hello()

print("Object 1: ", obj_1)  # Object 1:  <__main__.Hello object at 0x0000023E3AA48050>
print("Object 2: ", obj_2)  # Object 2:  <__main__.Hello object at 0x0000023E3AA48090>

print("Class object 1: ", type(obj_1).__name__)  # Class object 1:  Hello
print("Class object 2: ", type(obj_2).__name__)  # Class object 2:  Hello

print("Object 1 == Object 2: ", obj_1 == obj_2)  # Object 1 == Object 2:  False
