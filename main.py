from stats import get_book_text, count_words, get_word_list, count_characters


def main():
    words = get_book_text("books/frankenstein.txt")
    word_list = get_word_list(words)
    num_words = count_words(word_list)
    num_letters = count_characters(word_list)
    print(f"Found {num_words} total words")
    print(num_letters)


main()
