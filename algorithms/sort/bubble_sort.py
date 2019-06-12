from typing import List


def bubble_sort(num_arr: List) -> List:
    for iteration in range(0, len(num_arr) - 1):
        for moving_index in range(0, len(num_arr) - 1 - iteration):
            print(f'iteration: {iteration}, moving_index: {moving_index}')
            if num_arr[moving_index] > num_arr[moving_index + 1]:
                temp = num_arr[moving_index]
                num_arr[moving_index] = num_arr[moving_index + 1]
                num_arr[moving_index + 1] = temp
            print(f'sorted array: {num_arr}')
    return num_arr


if __name__ == '__main__':
    test_arr1 = [9, 2, 3, 2, 10, 8, 7, 11, 4, 5, 2]
    print(f'original: {test_arr1}, sorted: {bubble_sort(test_arr1)}')
