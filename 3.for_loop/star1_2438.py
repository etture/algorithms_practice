# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
def star1(n):
    for num in range(1, n+1):
        star_string = ''
        for repeat in range(num):
            star_string += '*'
        print(star_string)


star1(10)
