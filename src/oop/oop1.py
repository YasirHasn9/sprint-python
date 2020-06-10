# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#

# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # this is the base
    pass


class FlightVehicle(Vehicle):
    pass


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass


class GroundVehicle(Vehicle):
    # this is class is instance object of the class Vehicle
    pass


class Car(GroundVehicle):
    # instance object of the class GroundVehicle
    pass


class Motorcycle(GroundVehicle):
    # instance object of the class GroundVehicle
    pass


# class Starship(Vehicle):
#     pass
