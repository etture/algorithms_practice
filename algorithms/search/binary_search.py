from typing import List


def binary_search(num_arr: List, to_find: int, start_index: int = 0) -> int:
    middle_index = len(num_arr) // 2

    # print(f'arr: {num_arr}, middle index: {middle_index}, middle: {num_arr[middle_index]}')

    if len(num_arr) == 0:
        return -1

    if len(num_arr) == 1:
        if num_arr[middle_index] != to_find:
            return -1

    if len(num_arr) == 2:
        if num_arr[middle_index] < to_find:
            return -1

    # Found
    if num_arr[middle_index] == to_find:
        return start_index + middle_index

    # Left-side
    elif num_arr[middle_index] > to_find:
        return binary_search(num_arr[:middle_index], to_find, start_index=start_index)

    # Right-side
    else:
        return binary_search(num_arr[middle_index + 1:], to_find, start_index=(start_index + middle_index + 1))


if __name__ == '__main__':
    test_arr1 = [2, 3, 4, 5, 7, 8, 9, 10, 11, 23, 33, 50, 72, 73, 77, 101]
    print(f'test_arr: {test_arr1}')
    print(f'to find: {3}, index: {binary_search(test_arr1, 3)}')
    print(f'to find: {9}, index: {binary_search(test_arr1, 9)}')
    print(f'to find: {77}, index: {binary_search(test_arr1, 77)}')
    print(f'to find: {73}, index: {binary_search(test_arr1, 73)}')
    print(f'to find: {78}, index: {binary_search(test_arr1, 78)}')
