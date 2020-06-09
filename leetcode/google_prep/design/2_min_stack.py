class MinStack:
    DEFAULT_MIN = 99999999

    def __init__(self):
        self.stack = list()
        self.min = self.DEFAULT_MIN

    def push(self, elem: int) -> None:
        if len(self.stack) == 0:
            self.min = elem
        else:
            if elem < self.min:
                self.min = elem
        self.stack.append((elem, self.min))

    def pop(self) -> None:
        self.stack.pop(-1)
        if len(self.stack) == 0:
            self.min = self.DEFAULT_MIN
        else:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == '__main__':
    min_stack = MinStack()

    # min_stack.push(-2)
    # min_stack.push(0)
    # min_stack.push(-3)
    # assert min_stack.getMin() == -3
    # min_stack.pop()
    # assert min_stack.top() == 0
    # assert min_stack.getMin() == -2
    
    min_stack.push(2147483646)
    min_stack.push(2147483646)
    min_stack.push(2147483647)
    assert min_stack.top() == 2147483647
    min_stack.pop()
    assert min_stack.getMin() == 2147483646
    min_stack.pop()
    assert min_stack.getMin() == 2147483646
    min_stack.pop()
    min_stack.push(2147483647)
    assert min_stack.top() == 2147483647
    assert min_stack.getMin() == 2147483647
    min_stack.push(-2147483648)
    assert min_stack.top() == -2147483648
    assert min_stack.getMin() == -2147483648
    min_stack.pop()
    assert min_stack.getMin() == 2147483647
