# Colour Library
COLOUR_NAMES = {"aliceblue": "#f0f8ff", "brown": "#a52a2a", "burlywood": "#deb887", "cyan": "#00ffff",
                "green": "#006400", "orange": "#ff8c00", "gray": "#030303", "pink": "#ff69b4", "blue": "#add8e6",
                "purple": "#9370db"}

# print(colour code)
colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").lower()
