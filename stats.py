def get_book_text():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
    return file_contents

def get_num_words():
    num_words = len(get_book_text().split())
    return num_words