list1 = [5, 8, 9, 5, 4]
if len(list1) == 0:
    print(list1)
    print(list1)
else:
    edited_list = len(list1) //2
    if len(list1) %2 != 0 :
        edited_list += 1
    result = [list1[:edited_list], list1[edited_list:]]

    print(result)
  #исправленный код