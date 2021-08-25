# def chess_order(n, m, arr):
#     for i in range(n):
#         for j in range(m):
#             if i % 2 == 0 and j % 2 == 1:
#                 arr[i][j] = '*'
#             elif i % 2 == 1 and j % 2 == 0:
#                 arr[i][j] = '*'
#     return arr
#
#
# r, c = map(int, input().split())
# use_matrix = [['.'] * c for _ in range(r)]
# out_matrix = chess_order(r, c, use_matrix)
# for i in out_matrix:
#     print(*i, end='\n')


# def binary_filling(n, m, arr):
#     counter = 0
#     for i in range(m):
#         for j in range(n):
#             counter += 1
#             arr[j][i] = counter
#     return arr
#
#
# r, c = map(int, input().split())
# use_matrix = [[0] * c for _ in range(r)]
# out_matrix = binary_filling(r, c, use_matrix)
# for i in range(r):
#     for j in range(c):
#         print(str(out_matrix[i][j]).ljust(3), end='')
#     print()


# (j == n - i - 1 or j == i) or

# def binary_filling_diag(n, arr):
#     for i in range(n):
#         for j in range(n):
#             if (j >= n - i - 1 and i >= j):
#                 arr[i][j] = 1
#             elif (j <= n - i - 1 and i <= j):
#                 arr[i][j] = 1
#
#
#     return arr
#
#
# n = int(input())
# use_matrix = [[0] * n for _ in range(n)]
# out_matrix = binary_filling_diag(n, use_matrix)
# for i in out_matrix:
#     print(*i, end='\n')


# def snack(n, m, arr):
#     counter = 0
#     for i in range(n):
#         for j in range(m):
#             counter += 1
#             if i % 2 == 0:
#                 arr[i][j] = counter
#             else:
#                 arr[i][m-j-1] = counter
#
#     return arr
#
# r, c = map(int, input().split())
# use_matrix = [[0] * c for _ in range(r)]
# out_matrix = snack(r, c, use_matrix)
# for i in range(r):
#     for j in range(c):
#         print(str(out_matrix[i][j]).ljust(3), end='')
#     print()



content = open('nums.txt', 'r', encoding='utf-8')
values_of_file = [str.strip() for str in content.readlines()]
len_values = len(values_of_file)
sum_values = 0

for i in range(len_values):
    try:
        sum_values += int(values_of_file[i])
    except ValueError:
        continue

print(sum_values)
content.close()