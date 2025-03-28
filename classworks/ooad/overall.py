# # # class Mlass:
# # #   __slots__ = "__name", "__age"

# # #   def __init__(self, name, age):
# # #     self.__name = name
# # #     self.__age = age




# # # m = Mlass("James", 49)

# # # # print(m)

# # # # class A:
# # # #   def __init__(self, name, age):
# # # #     self.name = ''
# # # #     self.age = 0


# # # # a = A("", 3)

# # # # print(a.__dict__)



# # # class Mlass:
# # #   __slots__ = "name", "age"


# # #   def __init__(self, name, age):
# # #     self.name = name
# # #     self.age = age




# # # m = Mlass("James", 49)

# # # # print(m.__dict__)

# # # print(dir(Mlass))
# # # print(m.age)
# # # print(m.name)




# # # class B:
# # #   pass

# # # # print("B's attributes:", dir(B))



# # # import sys

# # # # print("tuple's size", sys.getsizeof(tuple()))
# # # # print("dict's size", sys.getsizeof(dict()))


# # # # class Person:
# # # #   def __init__(self, name, age):
# # # #     self.name = name

# # # #     self.age = age


# # # # p = Person("James", 22)

# # # # ref = p.__dict__

# # # # del p
# # # print(ref)


# # class Person:
# #   __slots__ = "name", "age"


# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age



# # class Student(Person):
# #   pass


# # s = Student("James", 23)

# # p = Person("Bob", 23)

# # # print(s.__dict__)
# # # print(p.__slots__)
# # # print(s.__slots__)

# # # s.x = 23

# # # print(s.__dict__)



# # # class MyList(list):
# # #   pass


# # # m = MyList()

# # # m.x = 23

# # # print(m.__dict__)

# # # l = list()

# # # l.x = 23



# # class Student(Person):
# #   # __slots__ = "avg_score"
# #   def __init__(self, name, age, avg_score):
# #     super().__init__(name, age)

# #     print(self.__slots__)
# #     self.avg_score = avg_score



# # s = Student("James", 50, 99)


# # print(s.__slots__)

# # print(s.name)
# # # print(s.__dict__)
# # # s.x = 23



# # class A:
# #   def __init__(self, x):
# #     self.x = 12
# #     self.y = 23





# # class B(A):
# #   pass


# # b = B(12)

# # print(b.__dict__)


# # l = list()

# # # l.x = 23

# # __new__


# class Vector:

#   def __new__(cls, *args, **kwargs):
#     print("__new__ called...")
#     return super().__new__(cls)
  
#   def __init__(self, x, y):
#     print("__init__ called...")

#     self.x = x 
#     self.y = y



    

  

# v = Vector(1, 2)

# # print(dir(Vector))
# # print(help(Vector.__new__))


# v = Vector.__new__(Vector)
# print(v)

# v.__init__( 1, 2)


# def general(*args, **kwargs):
#   # 1. __new__
#   # 2. __init__
#   pass



class SingletonFile:
  __instance = None

  def __new__(cls, *args, **kwargs):
    if cls.__instance == None:
      cls.__instance = super().__new__(cls)
    return cls.__instance


  def __init__(self): 
    self.__file = open("file.txt", "w")


   

# s1 = SingletonFile()
# s2 = SingletonFile()

# print(s1 is s2)

# print(id(s1))
# print(id(s2))

# a = None
# b = None

# print(id(a))
# print(id(b))


# ls1 = [1, 2, 3]
# ls2 = [1, 2, 3]

# print(id(ls1))
# print(id(ls2))


# st1 = "hello"
# st2 = "hello"


# n1 = 1
# n2 = 1

# print(st1 is st2)



# class Singleton:
#   __flag = False


#   def __init__(self, x):
#     if Singleton.__flag == True:
#       return 
    
#     self.x = x
#     Singleton.__flag = True
#     print('__init__ called')


# class B:
#   pass

# class A:
#   def __new__(cls, *args, **kwargs):
#     return super().__new__(B)
  

# a = A()

# print(a)


# # di = {}

# # exec(
# # """
# # x = 12
# # print(x)
# # """, globals(), di
# # )

# # print(di)

# # print(type(A()))


def init(self, x, y):
  self.x = x 
  self.y = y


di = {
  "__init__": init,
  "get_x": lambda self: self.x
}

# """def __init__(self, x, y):
#   self.x = x
# """


# Mlass = type('Mlass', (object, ), di)

# print(Mlass)

# m = Mlass(1, 2)

# print(m.get_x())


# Mlass = type('Person', (), di)

# ob = Mlass(1, 2)
# print(ob)


# def repr_decorator(cls):

#   cls.__add__ = lambda self, other: 123

#   return cls

# @repr_decorator
# class Person:
#   pass


# # Person = repr_decorator(Person)

# p = Person()
# p2 = Person()

# print(p + p2)
