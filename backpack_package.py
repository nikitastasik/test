from operator import itemgetter


def get_input_data():
    input_date = [list(map(int, input().split()))]
    value_backpack = input_date[0][1]
    costs, volumes = [], []
    for _ in range(input_date[0][0]):
        for cost, volume in enumerate([list(map(int, input().split()))]):
            costs.append(volume[0])
            volumes.append(volume[1])
    print(f'costs:{costs}')
    print(f'volumes:{volumes}')
    return costs, volumes, value_backpack


def calc_costs_item():
    costs, volumes, value_backpack = get_input_data()
    costs_item = []
    for i in range(len(costs)):
        costs_item.append([costs[i], volumes[i], costs[i] / volumes[i]])
    sorted_c_2 = sorted(costs_item, key=itemgetter(2))
    print(sorted_c_2)
    return sorted_c_2, value_backpack


def packing_backpack():
    sorted_c_2, value_backpack = calc_costs_item()
    total_cost = 0
    while value_backpack > 0 and sorted_c_2:
        print(f'totаl cost{total_cost}')
        print(f'value backpack{value_backpack}')

        if sorted_c_2[-1][1] <= value_backpack != 0:
            value_backpack -= sorted_c_2[-1][1]
            total_cost += sorted_c_2[-1][0]
            sorted_c_2.pop(-1)
        elif sorted_c_2[-1][1] > value_backpack != 0:
            total_cost += sorted_c_2[-1][2] * value_backpack
            if sorted_c_2[-1][0] != 0:
                value_backpack = 0
            sorted_c_2.pop(-1)
        elif sorted_c_2[-1][1] == 0:
            sorted_c_2.pop(-1)
    return total_cost


print(f'{packing_backpack():.3f}')
# =  for i in range(input_date[0])]



# import random
# def what_to_steal(qty):
#     choose_from = []
#     for i in range(qty):
#         item = random.choice(['iPhone10', 'брюлики', 'бордо 1810-го года', 'яйца Фаберже', 'Моны Лиза',
#                               'шапки Мономаха', 'песок с Марса', 'челябинский метеорит',
#                               'экобиотворог', 'палладий', 'гречка', 'весенний воздух', 'лепестки роз'])
#         cost = random.randint(5, 20)
#         weight = random.randint(1, 10)
#         choose_from.append([item, cost, weight])
#     return choose_from
#
# def packing(max_weight, qty_available):
#     objects = what_to_steal(qty_available)
#     objects = sorted(objects, key = lambda x: x[1] / x[2], reverse = True)
#     weight = 0
#     cost = 0
#     result = []
# #пока не достигли максимального веса и еще не все украли
#     while (max_weight - weight) > 0 and len(objects) > 0:
# # мне пришлось написать условие, проверяющее, сколько еще товаров мы можем добавить,
# # но, наверное, это можно и попроще написать
# #если вес товара в рюкзаке и добавляемого товара меньше максимальной вместимости,
# #добавляем весь товар
#         if (weight + objects[0][2]) <= max_weight:
#             add_weight = objects[0][2]
#             add_cost = objects[0][1]
# #если мы можем добавить только часть следующего товара, то нужно посчитать,
# #на какую сумму добавляем
#         elif (weight + objects[0][2]) > max_weight:
#             add_weight = max_weight - weight
#             add_cost = round((objects[0][1] / objects[0][2] * add_weight), 2)
# # добавляем в "результат" название товара, его стоимость и вес, а затем удаляем
# # товар из ассортимента магазина
#         item = objects[0][0]
#         weight += add_weight
#         cost += add_cost
#         result.append([item, add_cost, add_weight])
#         del objects[0]