class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Format and return string"""
        text_str = "{} ({:d}) : ${:,.2f}".format(self.name, self.year, self.cost)
        return text_str

    def get_age(self):
        """Return current age"""
        current_year = 2018
        return current_year-self.year

    def is_vintage(self):
        """Check if it is vintage"""
        return self.get_age() >= 50

