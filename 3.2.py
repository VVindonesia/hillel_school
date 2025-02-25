L1 = []
if len(L1) > 0:
    popped_number = L1.pop ()
    L1.insert(0, popped_number)
print(L1)

L1 = []
if L1 == []:
    print("[]")
else:
    popped_number = L1.pop ()
    L1.insert(0, popped_number)
    print(L1)
