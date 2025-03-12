# import abc

# class Musician(abc.ABC):
#   pass


# class Musician:
#   @abc.abstractmethod
#   def play(self, item):
#     ...

# class Musician(abc.ABC):
#   @abc.abstractmethod
#   def play(self, item):
#     print("hello world")


# m = Musician()
# print(m)             


from abc import ABC, abstractmethod



class Vehicle(ABC):

  @abstractmethod
  def get_max_speed(self):
    return "180 km/h"
  
  @abstractmethod
  def start_engine(self):
    ...


class Car(Vehicle):
  def get_max_speed(self):
    return super().get_max_speed()
  
  def start_engine(self):
    return "start with key..."
  

class MotorCycle(Vehicle):
  def get_max_speed(self):
     return super().get_max_speed()
  
  def start_engine(self):
    return "start with touch id..."
  

class Plane(Vehicle):
  def get_max_speed(self):
    return "980 km/h"
  
  def start_engine(self):
    return "start with turbine..."
  

class Bicycle(Vehicle):
  def get_max_speed(self):
    return "20 km/h"
  
  def start_engine(self):
    return "start with feet..."
  


car = Car()

print(f"Car max speed", car.get_max_speed())


motor = MotorCycle()

print(f"MotorCycle max speed", motor.get_max_speed())

by = Bicycle()

print(f"Bicycle max speed", by.get_max_speed())


class SuperCar(Vehicle):
  def get_max_speed(self):
    return super().get_max_speed()
  
  def setColor(self, color):
    self.color = color

  def start_engine(self):
    ...

s = SuperCar()


  
  