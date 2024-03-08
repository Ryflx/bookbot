def main():
    book_path = "books/frankenstein.txt" 
    text = get_text(book_path)
    num_words = word_count(text) 
    letters_dict = count_letters(text)
    print(f"---Begin report of {book_path}---")
    print(f"{num_words} words found in document")
    dict_list = sort_on(letters_dict)
    sort_on(letters_dict)
   


def word_count(text):
    words = text.split()
    return len(words)

def get_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
def count_letters(text):
    letter_counts = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def extract_value(d):
    # Assuming each dictionary has a single key-value pair, extract the value.
    # This function will be used as the `key` argument in the sort method.
    return list(d.values())[0]
    
def sort_on(letters_dict):
    dict_list = [{k: v} for (k, v) in letters_dict.items()]
    dict_list.sort(reverse=True, key=extract_value)
    return(dict_list)

    



 
main()
