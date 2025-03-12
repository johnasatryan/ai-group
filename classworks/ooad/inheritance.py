# class A:
#   def __init__(self):
#     print("A init called")


# class B(A):
#   def __init__(self):
#     print("B init called")


# class C(A):
#   def __init__(self):
#     print("C init called")

# class D(B, C):
#   def __init__(self):
#     print("D init called")


# # obj = D()

# # class Person:
# #   def __init__(self, name, age):
# #     if(name == ""):
# #       raise ValueError("Name can't be empty")
# #     self.name = name
# #     self.age = age

# #   def __str__(self):
# #     return f"{type(self).__name__}({self.name}, {self.age})"
 
# # class Student(Person):
# #   pass
# #   def __init__(self, name, age, avg_score):
# #     Person.__init__(self, name, age)
# #     self.avg_score = avg_score



# # s = Student("James", 33, 90.2)
# # # print(s)

# # # print(dir(Student))
# # # print(type(s).__name__)
# # # print(s.__dict__)

# # # print(help(super))


# # class A:
# #   def __init__(self):
# #     print("A init called")


# # class B(A):
# #   def __init__(self):
# #     # A.__init__(self)
# #     super().__init__(5)
# #     # super().method()

# #     print("B init called")


# # class C(A):
# #   def __init__(self, x):
# #     self.x = x
# #     print("C init called")

# # class D(B, C):
# #   def __init__(self):
# #     # C.__init__(self, 22)
# #     # super().__init__(11)
# #     print("D init called")


# # d = D()
# # print(d.__dict__)

# # super() == super("your class Name", "self")

# # print(super())

# class Base:
#   pass

# b = Base()

# # print(super(Base, b).__str__())
# # print(help(super))



# # A <- B 
# # A <- C
# # B, C <- D

class A:
  def foo(self):
    print("A::foo")

class B(A):
    def foo(self):
      print("B::foo")

class C(A):
   def foo(self):
    print("C::foo")

class D(B, C):
  pass

class E(D):
  pass

class F(E, B):
  pass




print(F.mro())

# class A:
#   pass

# class B(object, A):
#   pass





# class Base:
#   def some(self):
#     print("Base::some")


# # class Derived1(Base):
# #   def some(self):
# #     print("Derived_1 some")

# # class Derived2(Base):
# #   def some(self):
# #     print("Derived_2 some")

# # class Child(Derived1, Derived2):
# #   pass

# # c = Child()
# # c.some()

# # print(c)