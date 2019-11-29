"""Nyan Soe"""


def main():
    password = get_password()
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    min_length = 8
    password = input("Please enter your password:")
    while len(password) < min_length:
        print("password should be at least {}".format(min_length))
        password = input("Please enter your password:")
    return password


main()