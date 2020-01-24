"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_filename = ""
    check_symbol = ["(", "_"]  # A list of symbols where uppercase must follow

    for count, character in enumerate(new_name):
        current_character = character
        substitute_character = current_character
        if count > 0:
            if previous_character in check_symbol:
                substitute_character = current_character.upper()
            elif current_character.isupper() and previous_character.islower():  # for example: sW
                substitute_character = "_" + current_character
        previous_character = current_character
        new_filename = new_filename + substitute_character
    return new_filename


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Loop through each file in the (current) directory
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            source = os.path.join(directory_name, filename)
            destination = os.path.join(directory_name, new_name)
            print("Renaming {} to {}".format(source, destination))
            os.rename(source, destination)


# main()
demo_walk()
