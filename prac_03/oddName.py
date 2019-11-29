"""Nyan Soe"""


def main():
    name = get_name()
    frequency = int(input("Please enter the frequency:"))
    print_letter(name, frequency)


def print_letter(name, frequency):
    words = name.split()
    for word in words:
        count = 1
        for character in word:
            if count == frequency:
                print(character)
            count += 1


def get_name():
    name = input("Your name:")
    name = name.strip()
    while name == "":
        print("Name can not be blank")
        name = input("Your name:")
        name = name.strip()
    return name


main()