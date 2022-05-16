# Example about function evaluation

def f(a:int, b:int)->int:
    a = b
    return a

def g() -> int:
    a = f("a", 0)
    return a

def h() -> int:
    b = "a"
    a = f(b, 0)
    return a

def i() -> int:
    a = f(0, 1)
    return a

def j() -> str:
    a = f(0, 1)
    return a
