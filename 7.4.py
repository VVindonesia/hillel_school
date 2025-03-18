def common_elements():
    plurality_3 = {i for i in range(100) if i % 3 == 0}
    plurality_5 = {i for i in range(100) if i % 5 == 0}
    return plurality_3 & plurality_5
print (common_elements())