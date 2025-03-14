def audit_auth(func):
    def wrapper(username, *args, **kwargs):
        print("Simulating authentication from database.")
        database = {"Adrien": {"Password": "1234"}}
        if username in database:
            print("Granted, account exists")
        else:
            print("Denied, no account")
        return func(username, *args, **kwargs)
    return wrapper

@audit_auth
def authentication(username, password):
    database = {"Huniity": {"Password": "1234"}}
    new_user = {"Password": password}
    logged = False

    if username not in database:
        database[username] = new_user
        print(f"{username} | User must create an account first.")
        logged = False
    else:
        print(f"{username} | Logged in with success!!!")
        logged = True
        return
    print(database)

if __name__ == "__main__":
    username = input("Please insert your username: ")
    password = input("Please insert your password: ")
    authentication(username, password)
