import string

user_input = input()
reworked_text = "".join(symbol for symbol in user_input if symbol not in string.punctuation)
prefinal_text = "".join(reworked_text.title().split())
final_text = "#" +   prefinal_text
if len(final_text)>140:
    final_text = final_text[:140]


print(final_text)




