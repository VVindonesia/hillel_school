list1 = []
if list1:
    even_numbers = list1[::2]
    list_sum = sum(even_numbers)
    multiplier = list1[-1]
    result = list_sum * multiplier
else: result = 0
print(result)

