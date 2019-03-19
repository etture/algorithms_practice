# 문제 설명
# 계좌에 들어있는 돈 일부를 은행에서 출금하고자 합니다. 돈 담을 지갑이 최대한 가볍도록 큰 금액의 화폐 위주로 받습니다.
#
# 돈의 액수 money가 매개변수로 주어질 때, 오만 원권, 만 원권, 오천 원권, 천 원권, 오백원 동전, 백원 동전, 오십원 동전, 십원 동전, 일원 동전 각 몇 개로 변환되는지 금액이 큰 순서대로 배열에 담아 return 하도록 solution 메서드를 완성해주세요.
#
# 제한사항
# money는 1 이상 1,000,000 이하인 자연수입니다.
# 입출력 예
# money	result
# 50237	[1, 0, 0, 0, 0, 2, 0, 3, 7]
# 15000	[0, 1, 1, 0, 0, 0, 0, 0, 0]
# 입출력 예 설명
# 입출력 예 #1
# 50,237원은 5만 원권 1매, 100원짜리 동전 2개, 10원짜리 동전 3개, 1원짜리 동전 7개로 만들 수 있습니다.
#
# 입출력 예 #2
# 15,000원은 만 원권 1매, 5천 원권 1매로 만들 수 있습니다.


fifty_thousand = 0
ten_thousand = 1
five_thousand = 2
one_thousand = 3
five_hundred = 4
one_hundred = 5
fifty = 6
ten = 7
one = 8


def solution(money):
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    answer[fifty_thousand] = money // 50000
    money = money - (50000 * answer[fifty_thousand])
    answer[ten_thousand] = money // 10000
    money = money - (10000 * answer[ten_thousand])
    answer[five_thousand] = money // 5000
    money = money - (5000 * answer[five_thousand])
    answer[one_thousand] = money // 1000
    money = money - (1000 * answer[one_thousand])
    answer[five_hundred] = money // 500
    money = money - (500 * answer[five_hundred])
    answer[one_hundred] = money // 100
    money = money - (100 * answer[one_hundred])
    answer[fifty] = money // 50
    money = money - (50 * answer[fifty])
    answer[ten] = money // 10
    money = money - (10 * answer[ten])
    answer[one] = money

    return answer