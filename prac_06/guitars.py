from prac_06.guitar import Guitar


def main():
    guitars = []
    name = "Start"
    while name:
        name = input("Name:")
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, " added.")


if __name__ == "__main__":
    main()