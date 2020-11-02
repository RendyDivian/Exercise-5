def remove_keys(mydict, keylist):
    for keys in keylist:
        if keys in mydict:
            mydict.pop(keys)
    return mydict

if __name__ == "__main__":
    dictionary = {"book":"1", "pen":"2", "eraser":"3", "pencil":"4"}
    key_list = ["book", "pen", "pencil"]
    print(remove_keys(dictionary, key_list))
