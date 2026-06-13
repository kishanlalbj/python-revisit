# abstriction means showing only the necessory behavipur and hiding  the implementation details
from abc import ABC, abstractmethod

class Vechicle(ABC):
    @abstractmethod
    def start(self):
        # Every child should have their own start method.
        pass

class Car(Vechicle):
    def start(self):
        print("Car starts with key")


class Bike(Vechicle):
    def start(self):
        print("Bike starts with self start button")


i20 = Car()
i20.start()


royal_enfield_classic = Bike()
royal_enfield_classic.start()