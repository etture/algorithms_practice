def fibonacci(limit):
    n2 = 1
    if limit >= 1:
        yield n2

    n1 = 0
    for _ in range(1, limit):
        n = n1 + n2
        yield n
        n1, n2 = n2, n
    
if __name__ == '__main__':
    for i in fibonacci(10):
        print(i)

    fib = fibonacci(100)
    for _ in range(10):
        next(fib)
    for n in range(10, 21):
        print(f'{n}th value: {next(fib)}')

    fib.close()