def main():
    book_path = "books/frankenstein.txt" 
    text = get_text(book_path)
    num_words = word_count(text) 
    print(f"{num_words} words found in document")


def word_count(text):
    words = text.split()
    return len(words)

def get_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
def count_letters(words):
    pass


 
main()
