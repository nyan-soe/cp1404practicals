from prac_06.guitar import Guitar


def main():
    guitars = []
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, " added.")

        name = input("Name:")

    print("These are my guitars:")

    for i, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""  # set vintage_string by using ternary operator
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


if __name__ == "__main__":
    main()
