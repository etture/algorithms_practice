# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
def printN(n):
    for num in range(1, n+1):
        print(num)


# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
def printNReverse(n):
    for num in range(n, 0, -1):
        print(num)


printNReverse(10)
