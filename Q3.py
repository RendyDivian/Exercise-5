def find_value(mydict, val):
    keylist = []
    for key in mydict:
        if val in mydict[key]:
            keylist.append(key)
        return keylist


if __name__ == "__main__":
    dictionary = {"book":"1", "pen":"2", "eraser":"3", "pencil":"4"}
    user_input = input("Value key:")
    print(find_value(dictionary, user_input))
