from stats import get_book_text, count_words


def main():
    words = get_book_text("books/frankenstein.txt")
    num_words = count_words(words)
    print(f"Found {num_words} total words")


main()
