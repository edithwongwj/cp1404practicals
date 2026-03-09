"""CP1404 Practical - Guitar class."""
import datetime

# We use the system clock so the age calculation is always correct, even in the future!
CURRENT_YEAR = datetime.datetime.now().year

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not (50 or more years old)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Sort Guitars by year (oldest to newest)."""
        return self.year < other.year