class Vehicle:
    def __init__(self, wheels, speed, distance) -> None:
        self.wheels = wheels
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed):
        if self.wheels >= 4:
            self.speed += speed
            self.distance += 10;
        print("Accelerating", self.speed)
  


class Car(Vehicle):
    def __init__(self, company, wheels, speed, distance):
        super().__init__(wheels, speed, distance)
        self.company = company
    

mycar = Car("hyndai", 4, 0, 0)

print(mycar.wheels)

mycar.accelerate(10)
mycar.accelerate(20)
mycar.accelerate(30)

