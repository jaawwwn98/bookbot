def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


def count_words(words: str) -> int:
    word_list = words.split()
    return len(word_list)


def main():
    words = get_book_text("books/frankenstein.txt")
    num_words = count_words(words)
    print(f"Found {num_words} total words")


main()
