from prac_08.taxi import Taxi


def main():
    taxi_prius = Taxi("Prius 1", 100)
    expected_milage = 40
    actual_milage = taxi_prius.drive(expected_milage)
    if actual_milage == expected_milage:
        print("It has reached the destination.")
    else:
        print("It can not reach the destination.")
    print(taxi_prius)

    taxi_prius.start_fare()
    expected_milage = 100
    actual_milage = taxi_prius.drive(expected_milage)
    if actual_milage == expected_milage:
        print("It has reached the destination.")
    else:
        print("It can not reach the destination.  It stops at {:d} km.".format(actual_milage))
    print(taxi_prius)


if __name__ == "__main__":
    main()
