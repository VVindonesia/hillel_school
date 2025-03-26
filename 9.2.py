def difference(*args):
    if len(args) < 2:
        return 0
    sorted_args = sorted(args)
    return round(sorted_args[-1] - sorted_args[0], 2)
print(difference(10.2, -2.2, 0, 1.1, 0.5))
#12.39...9 не корректно? в задании указано округлить, если будут проблемы, считать это за проблему?
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
