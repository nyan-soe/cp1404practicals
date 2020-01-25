"""Test wikipedia API"""
import wikipedia


def main():
    search_phrase = input("Please enter the search pharase:")
    search_phrase = search_phrase.strip()  # remove white spaces
    while search_phrase != "":
        try:
            wikipedia_summary = wikipedia.summary(search_phrase)
            wikipedia_page = wikipedia.page(search_phrase)

            print("Title: ", wikipedia_page.title)
            print("URL: ", wikipedia_page.url)
            print("Summary: ", wikipedia_summary)
        except wikipedia.exceptions.DisambiguationError:
            print("Please be more specific!")
        search_phrase = input("Please enter the search pharase:")
        search_phrase = search_phrase.strip()


if __name__ == "__main__":
    main()
