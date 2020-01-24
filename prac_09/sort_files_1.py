"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Sort file 1."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    list_of_extentions = set()
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        path, raw_file_extention = os.path.splitext(filename)
        file_extention = raw_file_extention[1:]  # remove dot(.)
        list_of_extentions.add(file_extention)

        try:
            os.mkdir(file_extention)
        except FileExistsError:
            pass

        if os.path.isdir(file_extention):
            shutil.move(filename, file_extention + '/' + filename)


main()
