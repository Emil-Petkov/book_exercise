class MyClass:
    def set(self, n):
        self.number = n

    def show(self):
        print("Number = ", self.number)


obj_1 = MyClass()
obj_2 = MyClass()

obj_1.set(100)
obj_2.set(200)

obj_1.show()
obj_2.show()

obj_1.number = 123
obj_2.number = 321

obj_1.show()
obj_2.show()

# Number =  100
# Number =  200
# Number =  123
# Number =  321
