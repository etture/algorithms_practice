
def triangle(total_cnt):
    cur_num = 1
    row_cnt = 1
    print_triangle(cur_num, row_cnt, total_cnt)


def print_triangle(cur_num, row_cnt, total_cnt):
    print_str = ''
    for i in range(row_cnt):
        print_str += f'{cur_num} '
        cur_num += 1
    print(print_str)
    if row_cnt >= total_cnt:
        return
    row_cnt += 1
    print_triangle(cur_num, row_cnt, total_cnt)
    print(print_str)


if __name__ == '__main__':
    triangle(4)
