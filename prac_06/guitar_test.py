"""CP1404 Practical - Testing Guitar class."""
from guitar import Guitar
import datetime

CURRENT_YEAR = datetime.datetime.now().year

def main():
    """Test the Guitar class logic."""
    # Create two guitars to test
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1512.9)

    # Calculate what the ages *should* be
    expected_gibson_age = CURRENT_YEAR - 1922
    expected_other_age = CURRENT_YEAR - 2013

    # Test get_age()
    print(f"{guitar.name} get_age() - Expected {expected_gibson_age}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {expected_other_age}. Got {other.get_age()}")

    # Test is_vintage()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")

if __name__ == '__main__':
    main()