"""CP1404/CP5632 Practical - Client code to use the Car class."""
from car import Car

def main():
    """Demo test code to show how to use car class."""
    # 1. Update the original car to have a name
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 2. Create a new Car object called "limo" with 100 fuel
    limo = Car("Limo", 100)

    # 3. Add 20 more units of fuel
    limo.add_fuel(20)

    # 4. Print the amount of fuel in the car
    print(f"Limo has fuel: {limo.fuel}")

    # 5. Attempt to drive the car 115 km
    limo.drive(115)

    # 6. Print the limo object to test the __str__ method
    print(limo)

if __name__ == '__main__':
    main()