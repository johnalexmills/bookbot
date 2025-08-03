from stats import count_characters, count_words

file = "./books/frankenstein.txt"


def main():
    book_text = get_book_text(file)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    print(f"{num_words} words found in the document")
    for char, count in char_count.items():
        print(f"'{char}': {count}")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


main()
