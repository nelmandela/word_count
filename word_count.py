def words(sentence):
    my_words =sentence.split(" ")
    my_dict = {}
    for word in my_words:
        my_dict[word] = my_words.count(word)
    return my_dict
