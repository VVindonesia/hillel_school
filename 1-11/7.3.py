def second_index(text, some_str):
    first_index = text.find(some_str)
    search_index = text.find(some_str, first_index + 1)
    return search_index if search_index != -1 else None
print(second_index("looking for second i", "i"))