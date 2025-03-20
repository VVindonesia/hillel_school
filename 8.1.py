def add_one(*args):
    next_step = int("".join(str(i) for i in args))
    next_step += +1
    return next_step
print (add_one(1, 2, 3, 9, 9, 9))