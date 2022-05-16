from typing import Optional

def f(a: Optional[str]) -> str:
	if a is None:
		return "None"
	return a

def g(a: str):
	b : Optional[str]
	b = a
