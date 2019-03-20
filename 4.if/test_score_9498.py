# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
from sys import stdin


def test_score(score_int):
    if score_int >= 90:
        print('A')
    elif score_int >= 80:
        print('B')
    elif score_int >= 70:
        print('C')
    elif score_int >= 60:
        print('D')
    else:
        print('F')


score = int(stdin.readline().rstrip())
test_score(score)

test_edit = "hi"
