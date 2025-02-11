eval
exec

# print(eval("a = 56"))

code = """
a = 5 
b = 65

def foo():
  return "hello"

"""

di = {}

exec(code, globals(), di)

# # print(di)
# print(di['foo']())
a = 66
# print(globals())
# print(locals())

# print(globals() == locals())
# print(globals() is locals())

# def some_foo(fn):
#   print(locals())
#   import time
#   a = 23
#   b = 25



# some_foo(33)


# def f1():
#   pass


# import fractions

# import sys

# print()


import index

index.foo()