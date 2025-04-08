
data_input1 = int(input())
first_number, rest = divmod(data_input1, 1000)
second_number, rest = divmod(rest, 100)
third_number, fourth_number = divmod(rest, 10)
print (first_number)
print (second_number)
print (third_number)
print (fourth_number)