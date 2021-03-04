def add(a,b):
    return a+b

def subs(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a/b

