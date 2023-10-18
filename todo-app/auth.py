def Login(name, password):
    """authenticates user"""
    if name == "admin" and password == "admin":
        return True;
    return False;

def SignUp(name, password):
    """Creates new user"""