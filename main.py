from stats import get_book_text, total_num_words , count_unique_characters


def main():
    print(f"Found {total_num_words(get_book_text('books/frankenstein.txt'))} total words")
    print(str(count_unique_characters(get_book_text('books/frankenstein.txt'))) + " unique characters")


main()