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
