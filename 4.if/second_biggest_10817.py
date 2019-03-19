# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
from sys import stdin


def print_second_biggest(first, second, third):
    num_list = [first, second, third]
    num_list.sort()
    print(num_list[1])


one, two, three = map(int, stdin.readline().rstrip().split(' '))
print_second_biggest(one, two, three)
