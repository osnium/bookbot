from stats import *

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_text = book_text.lower()
    print(book_text)
    word_count = get_num_words(book_text)
    letter_stats = get_letter_stats(book_text)
    print(letter_stats)

    


main()