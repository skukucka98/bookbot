def get_book_text(path_to_book):
    file_contents = None
    with open(path_to_book) as f:
        file_contents = f.read()    
    return file_contents

def get_num_words(path_to_book):
    num_words = len(get_book_text(path_to_book).split())
    return num_words

def get_character_count(path_to_book):
    count_dict = {}
    lower_text = get_book_text(path_to_book).lower()
    char_list = list(lower_text)
    for char in char_list:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_alpha_chars(path_to_book):
    char_dict = get_character_count(path_to_book)
    sorted_char_list = []
    for char in char_dict:
        if str(char).isalpha():
            dict = {}
            dict["char"] = char
            dict["num"] = char_dict[char]
            sorted_char_list.append(dict)
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list