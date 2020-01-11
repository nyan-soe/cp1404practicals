from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi_silver = SilverServiceTaxi("Hummer", 200, 2)
    print(taxi_silver)
    expected_milage = 18
    actual_milage = taxi_silver.drive(expected_milage)
    if actual_milage == expected_milage:
        print("It has reached the destination.")
    else:
        print("It can not reach the destination.")
    print(taxi_silver)

    print("The trip costs: ${:.2f}".format(taxi_silver.get_fare()))


if __name__ == "__main__":
    main()
