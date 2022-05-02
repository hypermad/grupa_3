"""
Proxy pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class AbstractCar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Car(AbstractCar):
    def drive(self) -> None:
        print("Car has been driven!")


class Driver:
    def __init__(self, age: int) -> None:
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver) -> None:
        self.car = Car()
        self.driver = driver

    def drive(self) -> None:
        if self.driver.age <= 18:
            print("Sorry, the driver is too young to drive.")
        else:
            self.car.drive()


driver = Driver(18)
car = ProxyCar(driver)
# car = Car()
car.drive()

driver = Driver(25)
car = ProxyCar(driver)
# car = Car()
car.drive()
