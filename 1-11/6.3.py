user_input = int(input())
while  user_input > 9:
    list1 = [int(i) for i in str(user_input)]
    result = 1
    for num in list1:
        result = result * num
    user_input = result
print(user_input)