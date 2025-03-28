


# # # # from abc import ABC, abstractmethod

# # # # class Musician(ABC):
# # # #   @abstractmethod
# # # #   def play(self)->str:
# # # #     ...


# # # # class Guitarist(Musician):
# # # #   def play(self, some_arg):
# # # #     return "Guitarist plays guitar"


# # # # def control(musician: Musician):
# # # #   pass




# # # # # class MyCustomMeta(type):
# # # # #   def __call__(cls, *args, **kwargs):
# # # # #     instance = cls.__new__(cls)
# # # # #     return instance.__init__(*args, **kwargs)




# # # # # p = Person("m1", 23)
# # # # # Question 1


# # # # def decorator(cls):
# # # #   from functools import wraps

# # # #   @wraps(cls)
# # # #   def wrapper(*args, **kwargs):
# # # #     print(f" class name is: {cls.__name__}")
# # # #     print(f"class attributes: ")
# # # #     for method in dir(cls):
# # # #       if not method.startswith("__"):
# # # #         print(f"- {method}")
# # # #     instance = cls(*args, **kwargs)
# # # #     print(f"instance properties: ")
# # # #     for key, value in instance.__dict__.items():
# # # #       print(f"{{{key}: {value}}}")
# # # #     return instance
# # # #   return wrapper


# # # # # class Decorator:
# # # # #   def __init__(self, ):
# # # # #     pass
# # # # # @decorator

# # # # class Decorator:
# # # #   def __init__(self, custom_class):
# # # #     self.custom_class = custom_class

# # # #   def __call__(self, *args, **kwargs):
# # # #     print(f" class name is: {self.custom_class.__name__}")
# # # #     print(f"class attributes: ")
# # # #     for method in dir(self.custom_class):
# # # #       if not method.startswith("__"):
# # # #         print(f"- {method}")

# # # #     instance = self.custom_class(*args, **kwargs)
# # # #     print(f"instance properties: ")
# # # #     for key, value in instance.__dict__.items():
# # # #       print(f"{{{key}: {value}}}")

  

# # # # @Decorator
# # # # class Person:
# # # #   count = 0
# # # #   def __init__(self, name, age):
# # # #     self.name = name
# # # #     self.age = age

# # # #   def speak(self):
# # # #     print('Person speaks...')

# # # #   def sleep(self):
# # # #     print('Person sleeps')

# # # # print(Person)
# # # # # p = Person("James", 12)




# # # # # class Mlass:
# # # # #   def __init__(self, some_function):
# # # # #     self.some_function = some_function

# # # # #   def __call__(self, *args, **kwargs):
# # # # #     return self.some_function(*args, **kwargs)
  

# # # # def f(cls):
# # # #   print("before class I called this function")
# # # #   return cls

# # # # @f
# # # # class Vector:
# # # #   def __init__(self, x, y):
# # # #     self.x = x
# # # #     self.y = y



# # # # Question 2

# # # class Ab:
# # #   count = 0

# # #   def __init__(self):
# # #     Ab.count += 1
  
# # #   @classmethod
# # #   def foo(cls):
# # #     print('class method was called...')
# # #     print(cls.count)

# # #   @staticmethod
# # #   def st_foo():
# # #     print('static method')



# # # a = Ab()
# # # b = Ab()
# # # c = Ab()

# # # Ab.foo()
# # # a.foo()

# # # a.st_foo()
# # # Ab.st_foo()


# # # Question 4

# # from abc import ABC, abstractmethod

# # class Animal(ABC):
# #   @abstractmethod
# #   def speak(self):
# #     ...

# # class Dog(Animal):
# #   def speak(self):
# #     return 'haf haf'



# # class Cat:
# #   def speak(self):
# #     return 'meow'
  

# # # Animal.register(Cat)
# # # print(Cat.mro())
# # # print(issubclass(Dog, Animal))
# # # print(issubclass(Cat, Animal))


# # class Box:
# #   def __init__(self):
# #     print("Box ")
# #     self.__width = 0
# #   def get_width(self):
# #     return self.__width
# #   def set_width(self, w):
# #     self.__width = w

# # class Box2D(Box):
# #   def __init__(this):
# #     print("Box2D")
# #     super().__init__()
# #     this.__height = 0

# #   def get_height(this):
# #     return this.__height
# #   def set_height(this, h):
# #     this.__height = h

# # b1 = Box() # Box
# # b2 = Box2D() # Box2D, Box
# # b2.set_width(12)
# # b1.set_height(12)
# # print(b2.get_width(), b2.get_height())

# def foo(a):
#   pass

# def foo(a, b):
#   pass



# # class X: # -> [X, object]
# #   pass

# # class Y:# -> [Y, object]
# #   pass

# # class Z:# -> [Z, object]
# #   pass

# # class A(X, Y): # -> [X, Y, object]
# #   pass

# # class B(Y, Z): # -> [Y, Z, object]
# #   pass

# # class M(B, A, Z): # [Y, Z, object, X, Y, object, Z, object]
# #   pass



# class Vector:
#   def __init__(self, x, y):
#     self.x = x 
#     self.y = y

#   def __eq__(self, other):
#     if isinstance(other, Vector):
#       return self.x == other.x and self.y == other.y
  
#   def __hash__(self):
#     return hash(self)
  
#   def __le__(self, other):
#     pass

#   def __imull__(self, other):
#     if isinstance(other, tuple) and len(other) == 2:
#       other = Vector(*other)
    
#     if isinstance(other, Vector):
#       self.x *= other.x
#       self.y *= other.y



# class Base:   # -> [Base, object]
#     def __init__(self):
#         print("Base initializer")

#     def foo(self):
#         return "foo() called"

# class DerivedA(Base): # [DerivedA, Base, object]
#     def foo(self):
#         return "DerivedA foo() called"

# class DerivedB(Base):  # [DerivedB, Base, object]
#     def foo(self):
#         return "DerivedB foo() called"

# class DerivedC(DerivedA, DerivedB):  # [DerivedA, DerivedB, Base, object]
#     pass

# class DerivedD(DerivedB, DerivedA):
#     def foo(self):
#         return "DerivedD foo() called"

# objC = DerivedC()
# objD = DerivedD()

# print(objC.foo())
# print(objD.foo())


def TypeChecker(cls):
  def wrapper(*args, **kwargs):       
    results = zip(cls.__annotations__.values(), args)

    for key, value in results:
       if type(value) != key:
          raise TypeError("esinch er...")
  return wrapper

@TypeChecker
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age



p = Person(123, 23)