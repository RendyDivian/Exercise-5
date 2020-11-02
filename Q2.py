def accept_login(users, username, password):
    if username in users:
        if users[username] == password:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    dictionary = {"Rendy1": "asd123", "Rendy2": "asd321"}
    username = input("Username: ")
    password = input("Password: ")
    print(accept_login(dictionary, username, password))
