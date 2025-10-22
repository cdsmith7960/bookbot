from stats import char_count, get_num_words, sort_characters
import sys

def get_book_text(file_path) -> str:
    with open(file_path) as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")

    char_counts = char_count(book_text)
    for char_info in sort_characters(char_counts):
        print(f"{char_info['character']}: {char_info['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()