from stats import get_num_words

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")


main()