def get_book_text(filepath):
    with open(filepath, 'r') as file:
        filecontent = file.read()
    return filecontent


def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(book_text)


main()