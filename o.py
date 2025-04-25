# Base Class - Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived Class - Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Derived Class - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Derived Class - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Create objects of different vehicles
car = Car()
plane = Plane()
boat = Boat()

# Call the move() method on each object
car.move()    # "Driving"
plane.move()  # "Flying"
boat.move()   # "Sailing"
