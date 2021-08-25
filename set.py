# my_set = set()
# print(my_set)
# print(type(my_set))
#
# my_set.add(1)
# print(my_set)
# my_set.add(2)
# my_set.add(2)
# print(my_set)
#
# my_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4]
# s = set(my_list)
# print(s)
# print(len(s))


# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set2.issuperset(set1))
# print(set1.isdisjoint(set2))



# set1 = {1, 2, 3, 4}
# set2 = {1, 2,3 ,4 ,5}
# print(set1.union(set2))
# print(set1.intersection(set2))

set1 = {0, 1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
set1.update(set2)
print(set1)

# set1.remove(1)
# print(set1)
# set1.remove(42)
# print(set1)

set1.discard(2)
set1.discard(42)
print(set1)











