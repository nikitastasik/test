def greedy_algorithm(lst):
    sorted_list = sorted(lst)
    print(sorted_list)
    res_section = []
    i = 0
    n = len(sorted_list)
    while i < n:
        a = sorted_list[i]
        b = sorted_list[i] + 1
        res_section.append([a, b])
        i += 1
        while i < n and sorted_list[i] <= b:
            i += 1


    return res_section


print(greedy_algorithm([0.5, 2, 1, 3.5, 10, 0.7, 1.2]))
