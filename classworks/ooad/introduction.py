# class Another:
#   pass

# obj = Another()
# obj.x = 23
# print(obj.__dict__)

# obj2 = Another()
# print(obj2.__dict__)

# ls = list('hello')
# print(ls)

# ls.x = 23


# def foo():
#   pass

# foo.x = "hello"

# print(foo.__dict__)


# print(object)

ls = []
tp =(1,)
di = {}

class Person:
  pass


# p = Person()

# print(isinstance(tp, object))
# print(isinstance(ls, object))
# print(isinstance(di, object))
# print(isinstance(p, object))


# print(list.mro())
# print(Person.mro())


# class Person(object):
#   def setName(self, name):
#     self.name = name

#   def anotherBadSetName(name):
#     print(">>>>>>>>", name)
  


# # print(dir(Person))
# p = Person()

# p.setName("james")
# print(p.__dict__)

# # p.anotherBadSetName("Brad")
# # Person.anotherBadSetName(p, "Brad")
# p.anotherBadSetName()




class Car:
  def setModel(self, model):
    print("In Class <<<<<<", self)
    if model == "":
      raise ValueError("error")
    self.model = model


# c = Car()
# c.setModel("Audi")
# some_model = input("Enter model of car: ")
# if some_model == "":
#   raise ValueError
# c.model = ""
# print("Outside Class >>>>>>", c)


class Car:
  model = "Audi"


c = Car()

print(c.model)
print(c.__dict__)
print(dir(Car))