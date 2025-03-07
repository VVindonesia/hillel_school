import string
user_input = input()
for symbol in string.punctuation:
    user_input = user_input.replace(symbol, "")
final_text = "#" + "".join(letter.capitalize() for letter in user_input.split())
if len(final_text)>140:
    final_text = final_text[:140]
print(final_text)
