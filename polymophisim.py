class Vehicle:
    def move(self):
        """Base method to be overridden."""
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

# Function to demonstrate polymorphism
def vehicle_movement(vehicle):
    print(vehicle.move())

# Creating instances of each vehicle
my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()

# Demonstrating polymorphism
vehicle_movement(my_car)      # Output: Driving 🚗
vehicle_movement(my_plane)    # Output: Flying ✈️
vehicle_movement(my_bicycle)  # Output: Pedaling 🚲
