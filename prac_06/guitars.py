"""CP1404 Practical - Client program to use the Guitar class."""
from guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        # Create the new guitar object and add it to the list
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.\n")

        name = input("Name: ")

    # Uncomment the following two lines for quick testing so you don't have to type them every time!
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    if guitars:  # This checks if the list is not empty
        print("\nThese are my guitars:")
        # enumerate(guitars, 1) starts the counter 'i' at 1 instead of 0
        for i, guitar in enumerate(guitars, 1):
            # Using a ternary operator for the vintage string
            vintage_string = " (vintage)" if guitar.is_vintage() else ""

            # >20 means right-align in 20 spaces. 10,.2f means 10 spaces, with commas, 2 decimal places.
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go buy one!")


if __name__ == '__main__':
    main()