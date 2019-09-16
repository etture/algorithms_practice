import sys
sys.path.append('/Users/jinoo/Documents/Dev/algo_practice')
import math
import datetime
import dateutil.parser as datetime_parser
import heapq

from utils.Tester import Tester, Logger

'''
Input `lines`: 
[
2016-09-15 01:00:04.001 2.0s,
2016-09-15 01:00:07.000 2s
]
Output: int
'''

logger = Logger(verbose=False)

class Interval:
    def __init__(self, end_datetime, duration):
        self.duration = duration - 0.001
        dur_whole = math.floor(self.duration)
        dur_decimal = int(round(self.duration - dur_whole, 3) * 1000 * 1000)
        if isinstance(end_datetime, datetime.datetime):
            self.end_datetime = end_datetime
        else:
            self.end_datetime = datetime_parser.parse(end_datetime)
        self.start_datetime = self.end_datetime - \
            datetime.timedelta(seconds=dur_whole, microseconds=dur_decimal)

    def in_interval(self, interval):
        if interval.start_datetime <= self.start_datetime \
                <= interval.start_datetime + datetime.timedelta(microseconds=999000):
            logger.log(f'self.start_datetime: {self.start_datetime}, interval.start_datetime: {interval.start_datetime}')
            return True
        elif interval.end_datetime - datetime.timedelta(microseconds=999000) \
                <= self.end_datetime <= interval.end_datetime:
            logger.log(f'self.end_datetime: {self.end_datetime}, interval.end_datetime: {interval.end_datetime}')
            return True
        else:
            logger.log(f'voyaging through the void... self.end_datetime: {self.end_datetime}, interval.end_datetime: {interval.end_datetime}')
            return False

    def eligible_one_sec_intervals(self):
        intervals = []
        start_point = self.start_datetime - datetime.timedelta(microseconds=999000)
        while start_point <= self.end_datetime + datetime.timedelta(microseconds=999000):
            intervals.append(start_point)
            start_point += datetime.timedelta(microseconds=1000)
        return intervals

    def __repr__(self):
        return f'<Interval->start_datetime: {self.start_datetime}, end_datetime: {self.end_datetime}>'

def transform_logs_to_intervals(lines):
    intervals = []
    for line in lines:
        spl = line.split(' ')
        interval = Interval(' '.join([spl[0], spl[1]]), float(spl[2].split('s')[0]))
        intervals.append(interval)
    return intervals

def v1(lines):
    '''
    brute force
    1ms 마다 모두 돌려보기 때문에 비효율적
    '''
    intervals = transform_logs_to_intervals(lines)
    eligible_start_points = set()
    for intrvl in intervals:
        eligible_start_points.update(intrvl.eligible_one_sec_intervals())
    max_request = 0
    for start_point in eligible_start_points:
        cur_interval = Interval(start_point, 1)
        cnt = 0
        for intrvl in intervals:
            if intrvl.in_interval(cur_interval):
                cnt += 1
        if cnt >= max_request:
            max_request = cnt
    return max_request

def v2(lines):
    '''
    로그 시작과 끝 부분에서 1초 간격 내에 열려 있는 요청 개수만 계산
    로그 사이에 빈 공간은 스킵
    '''
    intervals = transform_logs_to_intervals(lines)
    interval_map = {}
    start_points_backward = []
    start_points_forward = []
    end_points_backward = []
    end_points_forward = []
    for idx, intrvl in enumerate(intervals):
        logger.log(f'idx: {idx}, interval: {intrvl}')
        interval_map[idx] = intrvl
        start_points_backward.append(tuple([intrvl.start_datetime - \
                    datetime.timedelta(microseconds=999000), idx]))
        start_points_forward.append(tuple([intrvl.start_datetime, idx]))
        end_points_backward.append(tuple([intrvl.end_datetime - \
                    datetime.timedelta(microseconds=999000), idx]))
        end_points_forward.append(tuple([intrvl.end_datetime, idx]))
    logger.log(f'start_points_forward: {start_points_forward}')
    logger.log(f'start_points_backward: {start_points_backward}')
    # merged_start_points = list(heapq.merge(
    #                         start_points_backward, 
    #                         start_points_forward,
    #                         key=lambda x: x[0]
    #                         ))
    # merged_end_points = list(heapq.merge(
    #                         end_points_backward,
    #                         end_points_forward,
    #                         key=lambda x: x[0]
    #                         ))    
    merged_points = list(heapq.merge(
                            start_points_backward,
                            start_points_forward,
                            end_points_backward,
                            end_points_forward,
                            key=lambda x: x[0]
                            ))
    # logger.log(f'merged_start_points: {merged_start_points}')
    active_open_points = dict()
    active_close_points = dict()
    max_request = 0
    # for start_point in list(heapq.merge(merged_start_points, merged_end_points, key=lambda x: x[0])):
    for start_point in merged_points:
        logger.log(f'sp: {start_point}, aop: {active_open_points}, acp: {active_close_points}')
        keys_to_delete = []
        for key, cp in active_close_points.items():
            if cp[0] < start_point[0]:
                logger.log(f'key {key} must be deleted')
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del active_open_points[key]
            del active_close_points[key]
            logger.log(f'after deleting key {key} -> aop: {active_open_points}, acp: {active_close_points}')
        end_point = start_point[0] + datetime.timedelta(microseconds=999000)
        for idx, open_point in enumerate(start_points_forward):
            if open_point[0] <= end_point:
                active_open_points[open_point[1]] = open_point
            else:
                start_points_forward = start_points_forward[idx:]
                break
        for idx, close_point in enumerate(end_points_forward):
            if close_point[0] <= end_point:
                active_close_points[close_point[1]] = close_point
            else:
                end_points_forward = end_points_forward[idx:]
                break
        cnt = len(active_open_points.keys())
        if cnt >= max_request:
            logger.log(f'max: {cnt}, aop: {active_open_points}, acp: {active_close_points}')
            max_request = cnt
    return max_request

def solution(lines):
    if len(lines) < 2:
        return 1
    else:
        # return v1(lines)
        return v2(lines)

test_cases = [
    (["2016-09-15 00:00:00.000 3s"], 1),
    (["2016-09-15 23:59:59.999 0.001s"], 1),
    (["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"], 1),
    (["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"], 2),
    (["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"], 7),
    (["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"], 1)
]

if __name__ == '__main__':
    tester = Tester(func=solution)
    for case in test_cases:
        tester.run_test(input=case[0], output=case[1])
    tester.summary()