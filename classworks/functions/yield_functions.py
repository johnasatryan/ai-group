# def makeActions():
#   acts = []

#   for i in range(5):
#     acts.append(lambda x: i ** x)
#   return acts

# acts = makeActions()
# # print(acts[0](2))
# # print(acts[1](2))
# # print(acts[3](2))
# # print(acts[4](2))

# # def foo():
# #   return "foo"

# # def bar():
# #   return "bar"

# # def fn():
# #   return "fn"

# # res = []

# # foo = lambda : "foo"
# # bar = lambda : "bar"
# # fn = lambda : "fn"
# res = []

# strings = ["foo", "bar", "fn"]

# # for i in range(5):
# #   res.append(lambda : strings[i])


# # print(res)
# # res[0]()
# # res[1]()
# # res[2]()

# def makeActions():
#   acts = []

#   for i in range(5):
#     acts.append(lambda x: i ** x)
#   return acts

# acts = makeActions()

# # print(acts[0](2))
# # print(acts[1](2))
# # print(acts[3](2))
# # print(acts[4](2))

# def closure():
#   i = 123
#   j = 234

#   def wrapper1():
#     nonlocal i
#     i += 1
#     return i

#   def wrapper2():
#     nonlocal j
#     j = 6454
#     return j
#   return wrapper1, wrapper2



# # some_functions = closure()

# # print(some_functions[0]())
# # print(some_functions[1]())
# # print(some_functions[0].__closure__)
# # print(some_functions[1].__closure__)


# def makeActions():
#   acts = []

#   for i in range(5):
    
#     acts.append(lambda x: i ** x)
#     print(f"{i}-rd iteration, {hex(id(i))}") 
#   return acts

# # acts = makeActions()
# # print(acts[0].__closure__)
# # print(acts[1].__closure__)
# # print(acts[2].__closure__)
# # print(acts[3].__closure__)

# # print(acts[0](2))
# # print(acts[1](2))
# # print(acts[3](2))
# # print(acts[4](2))

# # def actions():
# #   i = 16
# #   def a1():
# #     print(i)
# #   def a2():
# #     print(i)
# #   def a3():
# #     print(i)

# #   def a4():
# #     print(i)
# #   i = 64
# #   return [a1, a2, a3, a4]


# # acts = actions()

# # print(acts[0].__closure__)
# # print(acts[1].__closure__)
# # print(acts[2].__closure__)
# # print(acts[3].__closure__)

# # acts[0]()
# # acts[1]()
# # acts[2]()
# # acts[3]()


# def makeActions():
#   acts = []

#   for i in range(5):
    
#     acts.append(lambda x, a = i: a ** x)
#     print(f"{i}-rd iteration, {hex(id(i))}") 
#   return acts

# # acts = makeActions()
# # print(acts[0](4))
# # print(acts[1](4))
# # print(acts[2](4))
# # print(acts[3](4))
# # print(acts[0].__closure__)
# # print(acts[1].__closure__)
# # print(acts[2].__closure__)
# # print(acts[3].__closure__)
# arg = "hello"

# def foo(i = arg):

#   print(foo.__defaults__[0])
#   print(i)

# foo.__defaults__ = ("hello", )
# arg = 55
# foo(arg)



# # foo() 

# # print(foo.__defaults__)

# # import dis

# # print(dis.dis(foo))

# # print(help(zip))

# obj = zip([1, 2, 3], [4, 3], "hello")

# print(list(obj))

# def custom_zip(*iterables, strict = False):
#   min_length = min(len(item) for item in iterables)

#   if strict:
#     value = sum(len(item) for item in iterables)
#     if not value  == len(iterables) * min_length:
#       raise ValueError("xndirner")
#   return [tuple([iterable[i] for iterable in iterables]) for i in range(min_length)]


#   # for i in range(min_length):
#   #   # tmp = []
#   #   # for iterable in iterables:
#   #   #   tmp.append(iterable[i])
#   #   # res.append(tuple(tmp))


    
  


# print(custom_zip([1, 2, 3], [4, 3, 4], "hel", strict=True))

def custom_gen():
  yield 1

gen = custom_gen()

# print(list(gen))

# print(next(gen))
# print(next(gen))
##########################################
import time

def without_yield():
  res = []
  for i in range(10000000):
    res.append(i)

  return res

# def with_yield():
#   for i in range(10000000):
#     yield i

# start = time.time()
# res = without_yield()

# for i in res:
#   if i == 10000000 - 1:
#     print("gta ayd tive")
#     break

# print(f"Function without yield - duration: {time.time() - start}")

# start = time.time()

# res = with_yield()

# for i in res:
#   if i == 10000000 - 1:
#     print("gta ayd tive")
#     break

# print(f"Function without yield - duration: {time.time() - start}")


# def foo():
#   for i in range(5):
#     print("stex functione kangnec")
#     yield i
#     # kangnatsa 
#     print("stex functione sharunakec")

# gen = foo()

# print(next(gen))
# print(next(gen))


# def foo():
#   print("arajin kanch")
#   yield 1

#   print("erkrord kanch")
#   yield 2

#   print("es meke el yield chem ani")
#   print("nayeq chem arel")
#   yield 


# gen = foo()

# next(gen)
# next(gen)
# next(gen)
# next(gen)



def foo():
  for i in range(5):
    yield i



# gen = foo()

# print(next(gen))
# print(next(gen))
# gen.close()
# print(next(gen))

# print(foo())
# next(foo())

# print(next(foo()))


a = [x for x in range(10)]

b = (x for x in range(10))

# print(a)
# print(b)

def c_filter(function, iterable):
  if function is None:
    for i in iterable:
      if bool(i):
        yield i

  else:
    for i in iterable:
      if function(i):
        yield i

obj1 = filter(lambda x: x % 2 == 0, [x for x in range(10)])

# print(obj1)
# print(next(obj1))
# obj2 = c_filter(lambda x: x % 2 == 0, [x for x in range(10)])
# print(next(obj2))


# def some(arg):
#   if arg > 0:
#     return 65
#   else:
#     yield 23


# print(next(some(6)))

def foo():
  yield 1

  return 


foo()



