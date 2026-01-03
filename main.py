import sys

from stats import (
    get_book_text,
    count_words,
    get_word_list,
    count_characters,
    format_dict,
)


def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    words = get_book_text(book_path)
    word_list = get_word_list(words)
    num_words = count_words(word_list)
    num_letters = count_characters(word_list)
    formatted_count = format_dict(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for count in formatted_count:
        print(f"{count['char']}: {count['num']}")

    print("============= END ===============")


main()
