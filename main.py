from stats import get_num_words
from stats import get_character_count

def main():
    num_words = get_num_words()
    char_dict = get_character_count()
    print(f"{num_words} words found in the document")
    print(char_dict)

main()