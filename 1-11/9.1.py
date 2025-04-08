def popular_words(text, words):
    lowered_words = text.lower().split()
    result = {}
    for word in words:
        result[word] = lowered_words.count(word)
    return result
print(popular_words("I love THis WorLD World", ["love", 'world']))