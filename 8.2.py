def if_palindrome(text):
    return text == "".join(reversed(text))
print(if_palindrome("Fdg"))
#если делать через arghs, мне нужно кортеж в строку превращать?

def if_palindrome1(text):
    return text == text[::-1]
print(if_palindrome1("FdF"))