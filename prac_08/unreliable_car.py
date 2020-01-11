"""
CP1404/CP5632 Practical
UnreliableCar class
"""
import random
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance and depend on reliablility
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        chance = random.randint(0, 100)
        distance_driven = 0
        if chance < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
