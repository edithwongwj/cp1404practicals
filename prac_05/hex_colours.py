COLOUR_TO_CODE = {"Alizarin crimson", "#e32636", "Amaranth", "#e52b50", "Baby Pink", "f4c2c2"}

print(COLOUR_TO_CODE)
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()

print(COLOUR_TO_CODE)