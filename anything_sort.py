count_segments, count_points = map(int, input().split())
arr_segments = [list(map(int, input().split())) for i in range(count_segments)]
arr_points = list(map(int, input().split()))
first_points = list(map(lambda x: x[0], arr_segments))
last_points = list(map(lambda x: x[1], arr_segments))


def partition(points, low, high):
    pivot = points[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while points[i] < pivot:
            i += 1
        j -= 1

        while points[j] > pivot:
            j -= 1

        if i >= j:
            return j

        points[i], points[j] = points[j], points[i]


def quick_sort(points):
    def _quick_sort(points, low, high):
        if low < high:
            split_index = partition(points, low, high)
            _quick_sort(points, low, split_index)
            _quick_sort(points, split_index + 1, high)

    _quick_sort(points, 0, len(points) - 1)


sorted_first_points = quick_sort(first_points)
sorted_last_points = quick_sort(last_points)


def search_сoincidences_n(points, sorted_points, сoincidences):
    n = len(sorted_points)
    for i in points:
        count = 0
        for j in range(0, n):
            if sorted_points[j] <= i:
                count += 1
        сoincidences.append(count)

    return сoincidences

def search_сoincidences_m(points, sorted_points, сoincidences):
    n = len(sorted_points)
    for i in points:
        count = 0
        for j in range(0, n):
            if sorted_points[j] < i:
                count += 1
        сoincidences.append(count)

    return сoincidences


first_сoincidences = search_сoincidences_n(arr_points, first_points, [])
last_coincidences = search_сoincidences_m(arr_points, last_points, [])


def result(arr1, arr2):
    result_arr = []
    for i in range(0, len(arr1)):
        result_arr.append(arr1[i]-arr2[i])
    return result_arr

print(*result(first_сoincidences, last_coincidences))



