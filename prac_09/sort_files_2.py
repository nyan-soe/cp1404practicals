"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Sort file 2."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    list_of_extentions = set()
    directory_list_to_create = {}
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        path, raw_file_extention = os.path.splitext(filename)
        file_extention = raw_file_extention[1:]  # remove dot(.)
        list_of_extentions.add(file_extention)

    for extention in list_of_extentions:
        directory_extention = input("What category would you like to sort {} files into?".format(extention))
        directory_list_to_create[extention] = directory_extention  # Pair with extention and directory

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        path, raw_file_extention = os.path.splitext(filename)
        file_extention = raw_file_extention[1:]  # remove dot(.)

        new_directory = directory_list_to_create[file_extention]
        try:
            os.mkdir(new_directory)
        except FileExistsError:
            pass

        if os.path.isdir(new_directory):
            shutil.move(filename, new_directory + '/' + filename)  # move to the new directory


main()
