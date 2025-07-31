import sys
from stats import word_count, char_count, list_sort

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    print("============ BOOKBOT ============")
    try:
        filepath = sys.argv[1]
        print(f"Analyzing the book found at {filepath}")
        book_text = get_book_text(filepath)
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("----------- Word Count ----------")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    letter_count = char_count(book_text)
    letter_list = list_sort(letter_count)
    letter_list_length = len(letter_list)
    for i in range(0,letter_list_length):
        char = letter_list[i]
        character = char["char"]
        number = char["num"]
        print(f"{character}: {number}")
    print("============= END ===============")
main()
