def difference(*args):
    if args == 0:
        return 0
    sorted_args = sorted(args)
    return sorted_args[-1] - sorted_args[0]
print(difference(10.2, -2.2, 0, 1.1, 0.5))
#12.39...9 не корректно? в задании указано округлить, если будут проблемы, считать это за проблему?