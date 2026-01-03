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


def format_dict(character_counts: dict) -> list[dict]:
    formatted_list: list = []
    for char, num in character_counts.items():
        formatted_dict = {}

        formatted_dict["char"] = char
        formatted_dict["num"] = num
        formatted_list.append(formatted_dict)

    formatted_list.sort(reverse=True, key=sort_on)
    return formatted_list


def sort_on(items):
    return items["num"]
