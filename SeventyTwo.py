class Car:
    def drive(self):
        return "Driving car"

class Bike:
    def drive(self):
        return "Riding bike"

def vehicle_factory(vehicle_type):
    if vehicle_type == "car":
        return Car()
    if vehicle_type == "bike":
        return Bike()

v = vehicle_factory("car")
print(v.drive())
