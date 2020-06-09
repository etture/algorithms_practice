from typing import List

def mergesort(array: List[int]) -> List[int]:
    if len(array) == 1:
        return array
    else:
        divide_idx = len(array) // 2
        left = mergesort(array[:divide_idx])
        right = mergesort(array[divide_idx:])
        sorted_array = list()
        while len(left) > 0 or len(right) > 0:
            if len(left) == 0:
                sorted_array.extend(right)
                right = []
            elif len(right) == 0:
                sorted_array.extend(left)
                left = []
            else:
                smaller = left.pop(0) if left[0] < right[0] else right.pop(0)
                sorted_array.append(smaller)
        return sorted_array

def quicksort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    else:
        pivot_idx = len(array) // 2
        pivot = array[pivot_idx]
        left, right = list(), list()
        for idx, num in enumerate(array):
            if idx != pivot_idx:
                if num <= pivot:
                    left.append(num)
                else:
                    right.append(num)
        return quicksort(left) + [pivot] + quicksort(right)


if __name__ == '__main__':
    shuffled_1 = [9,8,3,2,5,4,1,7,6,0]
    shuffled_2 = [9,8,7,6,5,4,3,2,1,0]
    shuffled_3 = [0,1,2,3,4,5,6,7,8,9]
    shuffled_4 = [7,6,8,5,9,4,0,2,1,3]

    answer = [0,1,2,3,4,5,6,7,8,9]

    assert mergesort(shuffled_1) == answer
    assert mergesort(shuffled_2) == answer
    assert mergesort(shuffled_3) == answer
    assert mergesort(shuffled_4) == answer
    assert quicksort(shuffled_1) == answer
    assert quicksort(shuffled_2) == answer
    assert quicksort(shuffled_3) == answer
    assert quicksort(shuffled_4) == answer
    print(quicksort(shuffled_1))
    print(mergesort(shuffled_1))
