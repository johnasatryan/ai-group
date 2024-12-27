# # var  = 12

# # def foo():
# #   import sys
# #   mod = sys.modules['main']
# #   mod.var += 1


# # print(var)
  

# # def func(name, age, a = 0, b = 0):
# #   return a + b


# iterable = "he"
# iterable = [1, 2]
# iterable = (1, 2)
# iterable = {1, 2}
# iterable = {'name': 1, 'age': 5}



# # print(func(**iterable))

# # di = {'a' : 8, 'b' : 1}
# # print(func(**di))


# def func(name, age):
#   print(f"Name: {name}")
#   print(f"Age: {age}")


# # di = {"name": "James", "age": 30}

# # # for i in di.keys():
# # #   print(i)
# # func(**di.items())

# # def _foo():
# #   pass

# # adf = 23

# def func(*it, age = None):
#   if len(it[0]) > 2:
#     print(it[0][1])
#     return
#   print(age)


# my_list = ['spam', 'etc', 34]

# def example():
#   return None
#   x = 23
#   x += 55
#   print(x)

# # print(example())

# # func(my_list)

# # def foo(ls = []):
# #   ls.append((1, 3))
# #   print(ls)
# #   # return ls

# # print(foo())
# # print(foo())

# name = "James"

# # def foo(a, x = name, y = 23):
# #   print(x)


# # name = "Bob"

# # # print(dir(foo))
# # print(foo.__defaults__)


# def bar(a = []):
#   bar.__my_custom__default = (a, )
#   a.append(1)
#   print(a)


# # bar()
# # print(bar.__my_custom__default)
# # bar()
# # print(bar.__my_custom__default)


# # def some(a = set()):
# #   import random
# #   print(f"in local scope {id(a)}")
# #   a.add(random.randint(1, 100))
# #   print(f" after changing in local scope {id(a)}")

# #   print(a)


# # some()
# # some()
# # print(f"in global scope {id(some.__defaults__[0])}")


# def foo(ls = []):
#   ls.append((1, 2))

#   return ls

# ls = foo()

# print(ls)
# print(id(ls))
# print(id(foo.__defaults__[0]))

# ls.append("hello world")


# print(foo.__defaults__)

# x = 5

# # def foo():
# #   global x
# #   global x
# #   x = 3

# # foo()



# def f1():
#   x = 99

#   def f2():
#     x = "hello"

#     def f3():
#       x = 24
#     f3()
#   f2()
#   print(x)

# f1()

# x = 44

# def foo():
#   print(x)
#   x = 23

# foo()

# Recursion 

# def foo():
#   foo()


# foo()

# 1. Function call itself
# 2. Base case
# 3. Recursion msut solve problem divide the problem smaller once




# def foo(n):
#   if n < 0:
#     return
#   foo(n - 1)
#   print(n, end = ' ')


# foo(5)
# print()


