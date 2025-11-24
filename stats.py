def get_book_text(filepath):
    with open(filepath, 'r') as file:
        filecontent = file.read()
    return filecontent


def total_num_words(filecontent):
    words = filecontent.split()
    return len(words)

def count_unique_characters(filecontent):
    text = filecontent.lower()
    character_count = {}
    for char in text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count