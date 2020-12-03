# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#def a(x):
#return x**2
a = (lambda x: x ** 2)
print(a(10))

#def b(x, y):
#return math.sqrt(x**2 + y**2)
b = (lambda x,y: x**2 + y**2)
print(b(4,8))

#def c(*args):
#return sum(args)/len(args)
c = (lambda *args: sum(args)/ len(args))
print(c(4))

#def d(s):
#return "".join(set(s))
d = (lambda s: "".join(set(s)))
print(d("vwxyz"))


