import string
def correct_sentence(text):
    text = text.strip(".")
    text = text[0].upper() + text[1:]
    text += "."
    return text
print(correct_sentence("greetings, friends."))

