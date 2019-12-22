"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(visual_basic)  # display necessary information

    language_lst = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in language_lst:
        if language.is_dynamic():  # check if typing is dynamic
            print(language.name)


if __name__ == "__main__":
    main()
