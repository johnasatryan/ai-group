# count = 0

def counter(fn):
  count = 0
  def inner(x, y):
    nonlocal count;
    count += 1

    print(f'Function {fn.__name__} was called {count} times')

    return fn(x, y)
  return inner

def counter(fn):
  count = 0
  def inner(*args, **kwargs):
    nonlocal count;
    count += 1

    print(f'Function {fn.__name__} was called {count} times')

    return "baaa el inch kuzes"
  return inner
  
def add(a: int, b: int)->int:
  '''Adding two integers'''
  return a + b

def factorial(n: int)-> int:
  """
    Function calculates factorial of given number
  """
  if n <= 1:
    return 1
  return n * factorial(n - 1)


def mul(a: int, b:int, c:int = 1, *, d)->int:
  '''multipies 4 arguments'''
  return a * b * c * d

# decorated_add = counter(add)
# print(decorated_add(1, 3))
# print(add(1, 3))
# decorated_add(1, 3)
# decorated_add(1, 3)

# print(count)
# add(1, 3)
# add(1, 3)
# add(1, 3)

# print(count)

# add = counter(add)
# print(add)

# factorial = counter(factorial)
# print(factorial)

# factorial(5)

# print(mul(1, 2, 3, d = 4))

# print(help(mul))

# mul = counter(mul)
# print(help(mul))

# print(mul(1, 3, 4, d = 23))


# import inspect

# def counter(fn):
#   count = 0
#   def inner(*args, **kwargs):
#     nonlocal count;
#     count += 1
#     print(f'Function {fn.__name__} was called {count} times')
#     return fn(*args, **kwargs)
  
#   inner.__name__ = fn.__name__
#   inner.__doc__ = fn.__doc__
#   # inner.__annotations__ = fn.__annotations__
#   inner.__signature__ = inspect.signature(fn)
  

  return inner
  


# add = counter(add)
# print(help(add))


# print(help(factorial))
# factorial = counter(factorial)
# print(help(factorial))



# def foo(a: int, b: str) -> str:
#   "some animast function"
#   return b * a


# foo = counter(foo)
# print(help(foo))

# import functools

# def counter(fn):
#   count = 0
#   @functools.wraps(fn)
#   def inner(*args, **kwargs):
#     nonlocal count;
#     count += 1
#     print(f'Function {fn.__name__} was called {count} times')
#     return fn(*args, **kwargs)
#   return inner
  
 

# foo = counter(foo)
# # print(help(foo))


# def bar():
#   bar()


# bar()


# def factorial(n):
#   time.sleep(2)

import time


# start = time.time()

# factorial(543535345)

# print(time.time() - start)


def decorator(fn):
  def inner(*args, **kwargs):
    start = time.time()
    result = fn(*args, **kwargs)
    end = time.time()
    print(f'Function duration {(end - start): 2f} seconds')
    return result
  return inner



# def factorial(n):
#   time.sleep(2)


# # factorial(4)

# def fibonacci(n):
#   time.sleep(5)

# factorial = decorator(factorial)

# factorial(5)

# fibonacci = decorator(fibonacci)

# fibonacci(2)





def foo(a):
  print('hello world')
  print(a)


# foo = 23


# @foo
def bar():
  pass


# print(bar)

# bar = foo(bar)


# def some():
#   print('hello world')


# # @some
# def moo():
#   pass

# moo = some(moo)



def decorator(fn):
  def inner(*args, **kwargs):
    start = time.time()
    result = fn(*args, **kwargs)
    end = time.time()
    print(f'Function duration {(end - start): 2f} seconds')
    return result
  return inner


def counter(fn):
  count = 0
  def wrapper(*args, **kwargs):
    nonlocal count;
    count += 1
    print(f"Function {fn.__name__} was called {count} times")
    return fn(*args, **kwargs)
  return wrapper

# @counter
# @decorator
# def fibonacci(n):
#   time.sleep(1.345)
#   # return 1 if n <= 3 else fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci = decorator(fibonacci)
# fibonacci = counter(fibonacci)

# fibonacci(5)

def username_validator(fn):
  def wrapper(*args, **kwargs):
    if len(args) == 2:
      username = args[0]
      if not username:
        raise ValueError("Username can't be empty")

      return fn(*args, **kwargs)
  return wrapper

@username_validator
def login(username, password):
  print(f"hello {username}")


login("Bob", "")


