def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


def get_word_list(words: str) -> list[str]:
    return words.lower().split()


def count_words(word_list: list) -> int:
    return len(word_list)


def count_characters(word_list: list) -> dict[str, int]:
    character_counts = {}

    for word in word_list:
        for letter in word:
            if not letter.isalpha():
                continue
            elif letter not in character_counts:
                character_counts[letter] = 1
            else:
                character_counts[letter] += 1

    return character_counts
