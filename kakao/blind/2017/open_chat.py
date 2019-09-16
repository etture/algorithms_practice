import sys
sys.path.append('/Users/jinoo/Documents/Dev/algo_practice')

from utils.Tester import Tester, Logger

logger = Logger(verbose=True)

nicknames = {}

def process_record(tokens):
    command, uid = tokens[0], tokens[1]
    if command == 'Enter':
        nickname = tokens[2]
        nicknames[uid] = nickname
    elif command == 'Change':
        nickname = tokens[2]
        nicknames[uid] = nickname

def solution(record):
    tokens = []
    for rec in record:
        tokens.append(rec.split(' '))
        process_record(tokens[-1])
    answer = []
    for idx, rec in enumerate(record):
        command, uid = tokens[idx][0], tokens[idx][1]
        nickname = nicknames[uid]
        if command == 'Enter':
            answer.append(f'{nickname}님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(f'{nickname}님이 나갔습니다.')
    return answer

test_cases = [
    (["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"], ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])
]

if __name__ == '__main__':
    tester = Tester(func=solution)
    for case in test_cases:
        tester.run_test(input=case[0], output=case[1])
    tester.summary()