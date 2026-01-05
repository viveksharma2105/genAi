from functools import wraps
def req_admin(fun):
    @wraps(fun)
    def wrapper(user_role):
        if user_role != 'admin':
            print("Access denied!")
        else:
            return fun(user_role)
    return  wrapper

@req_admin
def auth(a):
    print ("authentication")
    
auth("user")