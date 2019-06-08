# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
# 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
# X보다 작은 수는 적어도 하나 존재한다.

from sys import stdin


def smaller_than_x(list_str, x):
    list_num = [int(num) for num in list_str.split(' ')]
    smaller_list = []
    for num in list_num:
        if num < x:
            smaller_list.append(num)
    print_list = ''
    for index, num in enumerate(smaller_list):
        if index == 0:
            print_list += str(num)
        else:
            print_list += (' ' + str(num))
    print(print_list)


n, x = map(int, stdin.readline().rstrip().split(' '))
list_str = stdin.readline().rstrip()
smaller_than_x(list_str, x)
