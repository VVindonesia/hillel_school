import string
import keyword

value = input()
if value[0].isdigit():
    print(False)
elif value in keyword.kwlist:
    print(False)
elif any(symbol in string.punctuation.replace("_", "") for symbol in value):
    print(False)
elif value.count("_")>1:
    print(False)
elif " " in value:
    print (False)
elif value != value.lower():
    print (False)
else: print(True)



