def main() -> None:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    
    print(count_words(file_contents))

def count_words(text: str) -> str:
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()