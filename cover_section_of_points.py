# from random import *
#
#
# def create_section(n):
#     lst = []
#     while len(lst) < n:
#         a = randint(0, 50)
#         b = a + randint(1, 10)
#         lst.append([a, b])
#     return lst
#
# from operator import itemgetter
#
# # [x_0, y_0], [x_1, y_1] так как сравниваем по сути два отрезка
# def greedy_algorithm_with_sorted_section(create_section):
#     res = create_section(n = int(input()))
#     sorted_res = sorted(res, key=itemgetter(1))
#     print(sorted_res)
#     finally_res = []
#     i = 0
#     finally_res.append(sorted_res[0])              #нужно удалять из массива данные, а не сравнивать пары. И последний добавленный всегда сравнивается со след. отр в оригинальном массиве. Если не
#                                                     #если не проходит проверку, то нахуй его. Если все ок, то он добавляется в массив и дальше сравнивается со следующим значением из оригинального масиива
#     while i < len(sorted_res)-1:
#             x_0 = sorted_res[i][0]
#             y_0 = sorted_res[i][1]
#             x_1 = sorted_res[i + 1][0]
#             y_1 = sorted_res[i + 1][1]
#             print(f'0 {x_0}, {y_0}')
#             print(f'1 {x_1}, {y_1}')
#             if (y_0 < x_1 and y_0 < y_1):
#                 finally_res.append(sorted_res[i+1])
#                 a = sorted_res[i][1]
#             i += 1
#     return finally_res
#
# print(greedy_algorithm_with_sorted_section(create_section))
#
#

# lst = [list(map(int, input().split()) for _ in range(n))]

from operator import itemgetter


def get_points():
    lst = []
    for _ in range(int(input())):
        lst.append(list(map(int, input().split())))

    sorted_lst = sorted(lst, key=itemgetter(1))
    return sorted_lst


def get_min_point(sorted_lst=get_points()):
    print(sorted_lst)
    res_lst = []
    i = 1
    while len(sorted_lst) > 1:
        a = sorted_lst[0][1]
        b = sorted_lst[i][0]
        c = sorted_lst[i][1]
        if c >= a >= b:
            if a not in res_lst:
                res_lst.append(a)
            sorted_lst.pop(i)
            print(f'sorted lst{sorted_lst}')
            print(f'res lst{res_lst}')

        elif a <= b <= c:
            if a not in res_lst:
                res_lst.append(a)
            sorted_lst.pop(0)
        else:
            sorted_lst.pop(0)

    if len(sorted_lst) == 1:
        if sorted_lst[0][1] not in res_lst:
            res_lst.append(sorted_lst[0][1])
            print('sdf')

    return res_lst

r = get_min_point()
print(len(r))
print(*r)


