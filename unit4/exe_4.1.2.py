def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat',
             'casa': 'house', 'el': 'the'}
    word_lst = sentence.split(' ')
    translator_generator = (words.get(word) for word in word_lst)
    translation = ""
    for translated_word in translator_generator:
        translation += translated_word + " "
    return translation


if __name__ == '__main__':
    print(translate("el gato esta en la casa"))