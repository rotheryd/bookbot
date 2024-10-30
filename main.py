def main() -> None:
    FILENAME = "books/frankenstein.txt"
    book_contents = read_book(FILENAME)
    words = count_words(book_contents)
    characters = count_characters(book_contents)
    char_list = convert_to_list(characters)
    char_list.sort(reverse=True, key=sort_on)

    create_report(FILENAME, words, char_list)

def create_report(name: str, word_count: int, characters: list[dict]) -> None:
    print(f"--- Begin report of {name} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in characters:
            char = item["character"]
            count = item["count"]
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def read_book(filename: str) -> str:
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(text: str) -> str:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    character_count: dict = {}
    for character in text:
        lower_char = character.lower()
        if lower_char in character_count:
            character_count[lower_char] += 1
        else:
            character_count[lower_char] = 1
    return character_count

def convert_to_list(count: dict) -> list[dict]:
    character_count: list[dict] = []
    for c in count:
        if c.isalpha():
            character_count.append({"character": c, "count": count[c]})
    return character_count

def sort_on(dict):
    return dict["count"]

if __name__ == "__main__":
    main()