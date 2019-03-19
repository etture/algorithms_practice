# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
def star3(n):
    for num in range(n, 0, -1):
        star_string = ''
        for repeat in range(num):
            star_string += '*'
        print(star_string)


star3(5)