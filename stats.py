def get_book_text():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
    return file_contents

def get_num_words():
    num_words = len(get_book_text().split())
    return num_words

def get_character_count():
    count_dict = {}
    lower_text = get_book_text().lower()
    char_list = list(lower_text)
    for char in char_list:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict