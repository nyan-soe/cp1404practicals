class ProgrammingLanguage:
    """Represent programming language object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Format and return string"""
        text_str = "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name,
                                                                                 self.typing, self.reflection,
                                                                                 self.year)
        return text_str
