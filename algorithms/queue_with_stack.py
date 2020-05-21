"""
Implement a queue using stacks
"""

class Queue:
    final_stack = list()
    temp_stack = list()

    def add(self, elem: int):
        while len(self.final_stack) > 0:
            self.temp_stack.append(self.final_stack.pop())
        self.final_stack.append(elem)
        while len(self.temp_stack) > 0:
            self.final_stack.append(self.temp_stack.pop())

    def pop(self):
        return self.final_stack.pop()


if __name__ == '__main__':
    q = Queue()
    q.add(3)
    q.add(4)
    q.add(12)
    q.add(2)
    print(f'q.final: {q.final_stack}')
    print(f'q.pop: {q.pop()}')
    print(f'q.final: {q.final_stack}')
    q.add(999)
    print(f'q.final: {q.final_stack}')