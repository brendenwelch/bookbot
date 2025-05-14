import sys
import stats as s


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}")
    book = s.get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = s.get_num_words(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = s.get_num_chars(book)
    sorted = s.sort(num_chars)
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()
