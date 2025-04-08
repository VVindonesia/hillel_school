list1 = [1, 0, 0, 3, 1, 0, 4]
nulls_count = list1.count(0)
while 0 in list1:
    list1.remove(0)
final_list = list1 + [0] * nulls_count
print (final_list)