def Login(name, password):
    """authenticates user"""
    if name == "admin" and password == "admin":
        return True;

def SignUp(name, password):
    """Creates new user"""