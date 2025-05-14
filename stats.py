def get_book_text(path):
    with open(path) as buf:
        return buf.read()


def get_num_words(book):
    word_list = book.split()
    return len(word_list)


def get_num_chars(book):
    lower = book.lower()

    char_count = {}
    for char in lower:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count


def sort(char_count):
    sorted = []
    for key in char_count:
        sorted.append({"char": key, "num": char_count[key]})
    sorted.sort(key=lambda d: d["num"], reverse=True)
    return sorted
