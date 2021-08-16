from typing import List


def bin_search(key: int, ary: List[int]):
    left: int = 0
    right: int = len(ary) - 1

    while left <= right:
        mid: int = left + (right - left) // 2
        if ary[mid] == key:
            return mid
        elif ary[mid] > key:
            right = mid - 1
        elif ary[mid] < key:
            left = mid + 1

    return -1


N = int(input())
W = []
for i in range(N):
    W += [int(input())]

key = int(input())

print(bin_search(key, W))
