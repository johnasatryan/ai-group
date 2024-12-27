# # def is_even(num):
# #   print('hello is_even function')
# #   return num % 2 == 0

# # def is_odd(num):
# #   return num % 2 != 0

# # def some_not_filter_func(x):
# #   print(x)

# # def custom_filter(func, iterable):
# #   res = []
# #   if func is None:
# #     for item in iterable:
# #       if bool(item) == True:
# #         res.append(item)
    
# #   # ended function
# #   else:
# #     for item in iterable: # [[1, 2, 3]]
# #       temp = func(item)
# #       if type(temp) != bool:
# #         raise ValueError('hargelis sxal tip es veradardznum...')
# #       if func(item) == True:
# #         res.append(item)
# #   return res


# # print(list(filter(lambda x : x % 2 == 0, [1, 0, 3, 0, 8, 14, 7])))

# # print(custom_filter(None, [0, 1, 6, 7, 0, False, True]))
# # print(custom_filter(is_even, [0, 1, 6, 7, 0, False, True]))
# # print(custom_filter(lambda x : x % 2 == 0, [1, 0, 3, 0, 8, 14, 7]))


# # # print(custom_filter(some_not_filter_func, "hello"))
# # print(custom_filter(None, "hello"))
# # print(list(filter(some_not_filter_func, "hello")))

# # # print(list(filter(is_odd, b"hello world")))



# # print(None % 2)


# # some_function = lambda x: print(x)

# # def some(x):
# #   if x % 2 == 0:
# #     print('even')
# #   else:
#     # print('odd')

# # lambda x: print(x)

# # some_func(6)

# # def filter(func, iterable):
# #   pass

# # filter(lambda x : x % 2 == 0, [])

# # lambda y: lambda x : x + 10


# predictions = [
#   {'tag': 'cat', 'coefficent': 0.91},
#   {'tag': 'dog', 'coefficent': 0.88},
#   {'tag': 'bird', 'coefficent': 0.5},
# ]


# # pred_filter_fn = lambda x: 
# # print(list(filter(pred_filter_fn, predictions)))

# # True if something else False

# def foo(x):
#   if type(x) == int:
#     print("ha inta")
#   else:
#     print("che int chi, chgitem el incha")

# foo("hello")
# foo(5)

# def foo(x):
#   print("ha inta") if type(x) == int else print("che int chi")


func = lambda x : print('x is int') if type(x) == int else print('x is not int')

# func(5)

def print_digits(n):
  if n < 0:
    return
  print(n)
  print_digits(n - 1)

# print_digits(5)

# pop = lambda x : None if x < 0 else pop(x - 1)

# print(pop(5))



def factorial(n):
  if n <= 1:
    return 1
  
  return n * factorial(n - 1)


# lambda_factorial = lambda x: 1 if x <= 1 else x * lambda_factorial(x - 1)

# print(lambda_factorial(5))

def foo(fn):
  fn()



# a = lambda x: lambda: print(x) 

# print(a.__annotations__)
# b = a(5)
# print(b.__closure__)




def add(x, y, z):
  return x + y + z

iterable1 = [1, 2, 3]
iterable2 = [4, 234, 5, 6]
iterable3 = [4, 5, 6]
iterable4 = [4, 5, 6]

# for i in range(len(iterable1)):
#   res = add(iterable1[i], iterable2[i])
#   print(f"{i + 1} iteration {res}")

def custom_min(a, b):
  return a if a < b else b

# def custom_map(func, iterable1, iterable2):
#   min_length = custom_min(len(iterable1), len(iterable2))

#   print(f"Minium length: {min_length} ")

#   res = []
#   for i in range(min_length):
#     tmp = func(iterable1[i], iterable2[i])
#     res.append(tmp)
#   return res


def custom_minimum_for_iterables(iterable):
  min_elem = iterable[0]
  for i in iterable[1:]:
    if min_elem > i:
      min_elem = i
  return min_elem


([4, 234, 5, 6], [1, 2], [542, 4])

def custom_map(func, *iterables):
  min_length = min([len(chlp) for chlp in iterables])
  res = []

  # for iterable in iterables[1:]:
  #   if min_length > len(iterable):
  #     min_length = len(iterable)
  # must be optimized to one line

  for i in range(min_length):
    tmp = []
    for iterable in iterables:
      tmp.append(iterable[i])
    res.append(func(*tmp))
  # optimization
  # return [[func(*iterable) for iterable in iterables] for i in range(min_length)]
      
iterable1 = [1]
iterable2 = [4, 234, 5, 6]
iterable3 = [4, 5, 6]
iterable4 = [4, 5, 6] 

# print(list(map(add, iterable1, iterable2, iterable3)))
print(custom_map(lambda x, y, z, e: x + y + z + e, iterable1, iterable2, iterable3, iterable4))
