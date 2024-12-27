# # def greet(name: str) -> None:
# #   print(f'hello {name}')
# #   def bar():
# #     print(name)

# #   bar()


# # # greet("James")


# # def foo():
# #   def bar():
# #     print('hello bar')
# #   return bar

# # # x = foo()

# # # print(x)

# # # x = print

# # # a = 6
# # # b = a


# # def foo():
# #   def bar():
# #     print('hello bar')
# #     return 99
    
# #   return bar


# # # print(foo())

# # x = foo

# # y = x()
# # z = y()

# # x = 5

# # print(hex(id(x)))

# # print(z)

# def f1():
#   x = 'hello'

#   y = 6
#   print(hex(id(y)))
#   def f2():
#     print(x)
#     print(y)

#   # print(f2.__closure__)
#   # return f2
#   f2()


# var = f1()

# # print(dir(var))

# print(var.__name__)
# print(var.__closure__)
# # print(var.__call__)

# def funcWrapper():
#   x = 23
#   def func():
#     x
#     pass

#   print(func.__closure__)
#   print(type(func.__closure__))

# funcWrapper()


def pow(n):
  def base(x):
    return x ** n
  return base
# square = pow(2)

# print(square(5))
# print(square(6))

# trip = pow(3)

# print(trip(5))
# print(trip(3))
# print(trip(4))


# def pow(n):
#   def base(x):
#     return x ** n
#   return base

# a = pow(5)


# a = 5
# print(hex(id(a)))
# s = func1(a)
# print(s.__closure__)

# import sys

# print(sys.getrefcount(a))


# def func1(a):
#   def func2():
#     print(a)  
#   return func2

# s1 = func1(7)
# s2 = func1(7)
# s3 = func1(9)
# s1.__closure__


# print(s1.__closure__)
# print(s2.__closure__)
# print(s3.__closure__)

# print(s1)
# print(s2)


def func1(a):
  def func2():
    nonlocal a
    a += 10
  
  def func3():
    func2
    print(a)    

  return (func2, func3)

tp = func1(5)

# print(tp[0].__closure__)
# print(tp[1].__closure__)
# print(id(tp[0]), id(tp[1]))


# def f1():
#   x = 23
#   def f2():
#     x 
#     def f3():
#       x

#     return f3
#   return f2

# func = f1()
# func2 = func()

# print(func.__closure__)
# print(func2.__closure__)


# def foo():
#   x = "hello"
#   def bar():
#     print(x)
#   return bar

# b = foo()
# b.__closure__[0].cell_contents = "bye"

# b()


def odd(nums: list) -> list:
  res = []
  for num in nums:
    if num % 2 != 0:
      res.append(num)

  return res

import random

ls = [random.randint(1, 100) for _ in range(10)]

# print(ls)
# print(odd(ls))


def some_method(x, y):
  return x % 2 == 0

# x = filter(some_method, ls)

# print(list(x))


def foo(a):
  return a + 1


def custom_filter(fn, iterable):
  res = []

  for i in iterable:
    if bool(fn(i)) == True:
      res.append(i)

  return res

x = custom_filter(foo, ls)
print(x)

# print(help(filter))