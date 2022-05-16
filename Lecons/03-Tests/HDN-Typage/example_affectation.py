# Examples about affectation
def f()->str:
 b = 0
 b = "b"
 return "a"

def g(a: int)->str:
 b = 0
 if a>0:
     b = "b"
 return "a"

def h(a)->str:
    b:int
    b = a
    return a
