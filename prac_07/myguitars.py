"""
CP1404 Practical 07 - More Guitars!
Read, add, sort, and save guitars.
"""
from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Manage a list of guitars loaded from and saved to a file."""
    guitars = []

    # 1. READ guitars from file
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            # parts[0] is name, parts[1] is year (int), parts[2] is cost (float)
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    # 2. ASK user for new guitars
    print("Add new guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        # Create a new Guitar object and add it to our list
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

        name = input("Name: ")

    # 3. SORT the guitars
    # This works because we added the __lt__ method to guitar.py!
    guitars.sort()

    # 4. DISPLAY the sorted guitars
    print("\nThese are my guitars:")
    for guitar in guitars:
        print(guitar)

    # 5. WRITE all guitars back to the file
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            # We save the raw data separated by commas, just like the original file
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    print(f"\nSaved {len(guitars)} guitars to {FILENAME}")


if __name__ == '__main__':
    main()