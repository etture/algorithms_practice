import time

# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
def sumN(n):
    sum = 0
    for num in range(1, n+1):
        sum += num
    print(sum)


def sumN2(n):
    if n % 2 == 0:
        print(int((1 + n) * (n // 2)))
    else:
        print(int((1 + n) * (n // 2) + (n + 1)/2))


start = time.time()
sumN(9999099)
sumNTime = time.time() - start
print(sumNTime)
# sumN2(9999099)
# sumN2Time = time.time() - start
# print(sumN2Time)

# sumN2 is much faster
