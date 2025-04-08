import string
user_range = input()
range_start, range_end = user_range.split("-")
final_range = ''.join(symbol for i in range(ord(range_start), ord(range_end) + 1) if symbol in string.ascii_letters)
print(final_range)
# пытался сделать через ord, но что-то не задалось