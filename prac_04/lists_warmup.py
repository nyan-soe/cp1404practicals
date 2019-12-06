def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers[0] = "ten"
    numbers[-1] = 1
    numbers_copy = numbers[2:]
    print(numbers_copy)
    if 9 in numbers:
        print("9 is in numbers")



if __name__ == '__main__':
    main()