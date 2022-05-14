# sets the maximum length to 10
def Maxlength(D):
    length = len(D)
    if(length >= 10):
        return 10
    if(length < 10):
        return length