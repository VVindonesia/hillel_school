def find_unique_value(*args):
    inclusive_uniques = []
    for i in args:
     if args.count(i) < 2:
         inclusive_uniques.append(i)
    return inclusive_uniques
print(find_unique_value(2, 2, 2, 5, 1, 8))
