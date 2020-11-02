def word_frequencies(mylist):
    dictword = {}

    for word in mylist:
        dictword.setdefault(word, 0)
        dictword[word] += 1
    return dictword


if __name__ == "__main__":
    user_input = input("Write your setence:")
    print(word_frequencies(user_input))
