class Dancer:

    def _left_foot_forward(self):
        print("Left forward")

    def _right_foot_forward(self):
        print("Right forward")

    def _left_foot_backward(self):
        print("Left backward")

    def _right_foot_backward(self):
        print("Right backward")

    def dance(self):
        self._left_foot_forward()
        self._left_foot_backward()
        self._right_foot_forward()
        self._right_foot_backward()
        self._left_foot_forward()
        self._right_foot_backward()
        self._left_foot_backward()
        self._right_foot_forward()


d = Dancer()

d.dance()
