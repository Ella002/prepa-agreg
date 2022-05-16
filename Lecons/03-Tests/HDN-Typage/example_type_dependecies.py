def f(b, c: str) -> int:
    a = b
    b = c
    return a

def g(b, c: str) -> int:
    b = c
    a = b
    return a

def f(a, b, c: str, d) -> int:
    while 1:
        a = b
        b = c
        if d():
            break
    return a

def g(a, b, c: str, d) -> int:
    while 1:
        b = c
        a = b
        if d():
            break
    return a
