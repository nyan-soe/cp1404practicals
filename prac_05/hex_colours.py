"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}
# print(STATE_NAMES)
for key, value in COLOR_CODES.items():
    print("{:3s} is {}".format(key, value))

color = input("Enter Color Name: ")
while color != "":
    #color = color.upper()
    if color in COLOR_CODES:
        print(color, "is", COLOR_CODES[color])
    else:
        print("Invalid color name")
    color = input("Enter Color Name: ")
