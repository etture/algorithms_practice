import time

class Tester:
    def __init__(self, func, test_cases=[]):
        self.func = func
        self.test_cases = test_cases
        self.counter = 1
        self.monitor = []

    @classmethod
    def factory(cls, test_cases, func):
        return cls(func, test_cases)

    def run(self, unordered_output=False):
        for case in self.test_cases:
            self.run_test(input=case[0], output=case[1],
            unordered_output=unordered_output)
        self.summary()

    def run_test(self, input, output, unordered_output=False):
        start = time.time()
        print('----------------------------------')
        print(f'Case {self.counter}')
        print(f'Input: {input}')
        print(f'Expected Output: {output}')
        result = self.func(input)

        if unordered_output:
            result_copy = result.copy()
            contains_same = False
            for op in output:
                if op not in result_copy:
                    print(f'Output: {result}\nCase FAILED--output should contain {output}')
                    self.monitor.append(self.counter)
                    self.counter += 1
                    end = time.time()
                    print(f'Time elapsed: {round(end-start, 4)} seconds')
                    return
                else:
                    result_copy.remove(op)
            if len(result_copy) > 0:
                print(f'Output: {result}\nCase FAILED--output should contain {output}')
                self.monitor.append(self.counter)
                self.counter += 1
                end = time.time()
                print(f'Time elapsed: {round(end-start, 4)} seconds')
            else:
                print(f'Output: {result}\nCase PASSED')
                self.counter += 1
                end = time.time()
                print(f'Time elapsed: {round(end-start, 4)} seconds')

        else:
            try:
                assert result == output, f'Output: {result}\nCase FAILED--output should be {output}'
            except AssertionError as e:
                print(e)
                self.monitor.append(self.counter) 
            else:
                print(f'Output: {result}\nCase PASSED')
            finally:
                self.counter += 1
                end = time.time()
                print(f'Time elapsed: {round(end-start, 4)} seconds')

    def summary(self):
        print('=============Summary==============')
        total_cases = self.counter - 1
        wrong_cases = len(self.monitor)
        correct_cases = total_cases - wrong_cases
        if wrong_cases == 0:
            print('Everything passed!')
        else:
            print(f'Failed cases: {self.monitor}')
        print(f'Score: {correct_cases}/{total_cases} == {round(float(correct_cases)/total_cases, 2)}')
        print('==================================')

class Logger:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def log(self, msg):
        if self.verbose:
            print(msg)

def test(num):
    return num

if __name__ == '__main__':
    tester = Tester()
    for num in range(3):
        if num == 2:
            tester.run_test(test, [num], [3])
        else:
            tester.run_test(test, [num], [num])

    print('everything passed')