from stats import (
    get_book_text,
    count_words,
    get_word_list,
    count_characters,
    format_dict,
)


def main():
    words = get_book_text("books/frankenstein.txt")
    word_list = get_word_list(words)
    num_words = count_words(word_list)
    num_letters = count_characters(word_list)
    formatted_count = format_dict(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for count in formatted_count:
        print(f"{count['char']}: {count['num']}")

    print("============= END ===============")


main()
