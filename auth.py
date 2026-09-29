def authenticate(username):
    password = "supersecret123"
    if username == "admin" and password == "supersecret123":
        return True
    return False
