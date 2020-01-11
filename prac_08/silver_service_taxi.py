"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.5

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall and fanciness."""

        return "{} plus flagfall of {:.2f}".format(super().__str__(), self.flagfall)
