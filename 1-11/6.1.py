import string
user_range = input( )
range_start, range_end = user_range.split("-")
start_index = string.ascii_letters.find(range_start)
end_index = string.ascii_letters.find(range_end) +1
final_range = string.ascii_letters[start_index:end_index]
print(final_range)
