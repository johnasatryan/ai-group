def enumerate_gen(iterable, start = 0):
  index = start
  for item in iterable:
    yield (index, item)
    index += 1

ls = [1, 2, 'hello']

enumm = enumerate_gen(ls, -534)

# print(list(enumm))

# print(help(range))

def _range_generator(stop):
  i = 0
  while i < stop:
    yield i
    i += 1


def __range_generator(start, stop, step=1):
  while (step > 0 and start < stop) or (step < 0 and start > stop):
    yield start
    start += step


def range_generator(*args):
  if len(args) == 1:
    return _range_generator(args[0])
  elif len(args) == 2 or len(args) == 3:
    return __range_generator(*args)
  else:
   raise TypeError("mer custom range kara stana at most 3 kam 4 argument")



# print(list(range_generator(-1, -5, -1, 56)))

def custom_map_with_yield(func, *iterables):
  iterators = [iter(it) for it in iterables]
  while True:
    try:
      elements = [next(it) for it in iterators]
      yield func(*elements)
    except StopIteration:
      break



def add(a, b, c):
  return a + b + c




# for elements in custom_map_with_yield(add, [1, 3, 4], (5, 6) , (11, 34, 1)):
#   print(elements)



def custom_filter_with_yield(func, iterable):
  # if func is None:
  #   for iter in iterable:
  #     if iter:
  #       yield iter
  # else:
  #   for iter in iterable:
  #     if func(iter):
  #       yield iter

  if func is None:
    func = bool
  
  for item in iterable:
    if func(item):
      yield item

# print(list(custom_filter_with_yield(None, [1, 0, False, "", 54])))




# print(list(custom_filter_with_yield(None, [1, 0, False, "", 54])))


# (1, 5, 11) & (3, 6, 34)

def custom_zip_with_yield(*iterables):
  iterators = [iter(it) for it in iterables]

  while True:
    try:
      yield tuple(next(item) for item in iterators)
    except (StopIteration, RuntimeError):
      break

# print(list(custom_zip_with_yield([1, 3, 4], (5, 6) , (11, 34, 1))))

# iterables = ([1, 3, 4], (5, 6) , (11, 34, 1))

# iterators = [iter(it) for it in iterables]

# while True:
#   print(tuple(next(it) for it in iterators))


# for elements in custom_zip_with_yield([1, 3, 4], (5, 6) , (11, 34, 1)):
#   print(elements)


# ls = [[15, 64, 23], [1, 2, 3], [4, 5, 6]]

# iterators = [iter(it) for it in ls]

# while True:
#   print(tuple(next(item) for item in iterators))



# def foo(a):
#   if a > 0:
#     return 453
#   else:
#     yield 2


# p = foo()
# next(p)

def repeat(n):
  def decorator(fn):
    def inner(*args, **kwargs):
      for i in range(n):
        fn(*args, **kwargs)
    return inner
  return decorator


 
@repeat(10)
def greet(): 
    print("Hello!")

# greet = decorator(greet, 5)

# old_greet = greet
# greet = repeat(8)

# greet = greet(old_greet)


# greet()

def memoize(fn):
  cache = {}
  def inner(n):
    if not cache.get(n):
      cache[n] = fn(n)
    print(cache)

    return cache[n]
  return inner
    



@memoize 
def factorial(n):
  if n <= 1:
    return 1
  return n * factorial(n - 1)

print(factorial(20))
# print(factorial(5))
# print(factorial(4))
# Output: 55 (calculated efficiently using caching)
