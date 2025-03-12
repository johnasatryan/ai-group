# # # class BankAccount:
# # #   def __init__(self, balance: float, id: str):
# # #     self.__balance = balance
# # #     self.id = id

# # #   def __repr__(self):
# # #     return f"Account balance: {self.__balance} - id: {self.id}"


# # # account1 = BankAccount(500.4, "123566")
# # # # print(account1.balance)
# # # # print(account1.id)
# # # print(account1)


# # # print(account1.__dict__)
# # # print(account1._BankAccount__balance)

# # # class BankAccount:
# # #   def __init__(self, balance: float, id: str):
# # #     # self.__balance = balance

# # #     self.setBalance(balance)
# # #     self.id = id

# # #   def getBalance(self):
# # #     return self.__balance
  
# # #   def getId(self):
# # #     return self.id
  

# # #   def setBalance(self, value):
# # #     if value < 0:
# # #       raise ValueError("Balance can't be negative...")
# # #     self.__balance = value


# # #   def __repr__(self):
# # #     return f"Account balance: {self.__balance} - id: {self.id}"


# # # account1 = BankAccount(-500.4, "123566")
# # # print(account1.balance)
# # # print(account1.id)
# # # print(account1.__dict__)

# # # print(account1.getBalance())

# # # account1.setBalance(100)
# # # print(account1.getBalance())

# # # account1.id = "2345346"


# # class BankAccount:

# #   def __generateUniqueId(self):
# #     import uuid

# #     return uuid.uuid4()
  
# #   def __init__(self, balance: float):
# #     # self.__balance = balance

# #     self.setBalance(balance)
# #     self.id = self.__generateUniqueId()

# #   def getBalance(self):
# #     return self.__balance
  
# #   def getId(self):
# #     return self.id
  

# #   def setBalance(self, value):
# #     if value < 0:
# #       raise ValueError("Balance can't be negative...")
# #     self.__balance = value


# #   def __repr__(self):
# #     return f"Account balance: {self.__balance} - id: {self.id}"
  


# # account1 = BankAccount(500.3)

# # print(dir(BankAccount))

# class Person:
#   def __init__(self, name, age):
#     self.__name = name
#     self.__age = age

#   @property
#   def name(self):
#     return self.__name
  
#   @name.setter
#   def name(self, value):
#     if value == "":
#       raise ValueError("esinch es poxancel....")
#     self.__name = value

#   @property
#   def age(self):
#     print("hello", self)
#     return self.__age
  
# p = Person("James", 44)
# print(p.name)

# name = input("Enter person name: ")
# age = input("Enter person age: ")

# p.name = name
# p.age = age


# print(p.__dict__)

# print(p.age)

# p.name = ""
  

# class Person:
#   def drink(self):
#     ...


# class A:
#   def drink(self):
#     print('hello A')


# print(issubclass(A, Person))

# from typing import Sized, Sequence

# print(issubclass(list, Sized))
# print(issubclass(list, Sequence))

# print(list.mro())


class Mlass:
  def __str__(self):
    print('kanchvec')
    return "inch vor ban"


ob = Mlass()



class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    result_x = self.x + other.x
    result_y = self.y + other.y

    result_object = Vector(result_x, result_y)
    return result_object 

  def __sub__(self, other):
    pass

  def __mul__(self, other):
    pass

  def __div__(self, other):
    pass 

  def __mod__(self, other):
    pass

  def __iadd__(self, other):
    pass




  def __repr__(self):
    return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 3)
v2 = Vector(4, 6)

# v3 = Vector(v1.x + v2.x, v1.y + v2.y)
v3 = v1 + v2


# v1 + v2 == v1.__add__(v2)
print(v3)

print(v2 + v1 + v3)



5 += 12
