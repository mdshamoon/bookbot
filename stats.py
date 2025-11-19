def get_words_count(text):
    words = text.split()
    return len(words)


def get_characters_count(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_list(chars_count):
    char_list = []
    for char in chars_count:
        char_list.append({"char": char, "num": chars_count[char]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list


