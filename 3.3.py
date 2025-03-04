list1 = [1, 2, 3]
if len(list1) == 0:
    print(list1)
    print(list1)
else:
    list_first_half = len(list1) //2
    if len(list1) %2 != 0 :
        list_first_half += 1
    list_second_half = [list1[:list_first_half], list1[list_first_half:]]
    print(list_first_half)
    print(list_second_half)
  #исправленный код