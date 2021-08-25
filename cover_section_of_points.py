
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


