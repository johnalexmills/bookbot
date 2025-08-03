def sort_dicts(dict_list: list) -> list:
    return dict_list.sort()

def count_characters(text: str) -> dict:
    char_count = {}
    text = text.lower()
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def count_words(text):
    return len(text.split())
