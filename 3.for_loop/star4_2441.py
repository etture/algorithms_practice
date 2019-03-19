# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
def star4(n):
    for num in range(n, 0, -1):
        star_string = ''
        blank_string = ''
        for star in range(num):
            star_string += '*'
        for blank in range(n - num):
            blank_string += ' '
        print(blank_string + star_string)


star4(7)
