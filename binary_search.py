n, *A = map(int, input().split())
k, *K = map(int, input().split())

from math import *


def binary_search(len_n, l_1, len_k, l_2):
    res = []
    for index, item in enumerate(l_2):
        print(f'item: {item}')
        print(res)
        l = 0
        r = len_n - 1
        while l <= r:
            mid = (l + r) // 2
            if l_1[mid] == item:
                res.append(mid+1)
                break
            elif l_1[mid] > item:
                r = mid - 1
            elif l_1[mid] < item:
                l = mid + 1
        if l > r:
            res.append(-1)

    return res


print(binary_search(n, A, k, K))

# for item, index in l_2:
#     mid = l_1[round(len_n / 2)]
#     print(mid)
#     if item == mid:
#         res.append(round(len_n / 2))
#     elif item < mid:
#         l_1 = l_1[:mid - 1]
#     elif item > mid:
#         l_1 = l_1[mid + 1:]
#     else:
#         return -1
