from stats import get_num_words
from stats import get_sorted_alpha_chars
import sys

def main():
    args = sys.argv

    if len(args) == 2:
        num_words = get_num_words(args[1])
        sorted_char_dict = get_sorted_alpha_chars(args[1])

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {args[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in sorted_char_dict:
            print(f"{dict["char"]}: {dict["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()