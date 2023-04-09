from collections import Counter

# This will be used in sorting a list of tuples later on. It will be the key to sort
def second_element(tuple):
    return tuple[1]

file_path = "books/frankenstein.txt"
with open(file_path) as f:
    
    contents = f.read()
    words = contents.split() # I will print the len of this out later

    lower_words = [s.lower() for s in words]
    counter = Counter("".join(lower_words))
    counter_dict = dict(counter)
    letters_dict = {}
    for key, value in counter_dict.items():
        if key.isalpha():
            letters_dict.update({key: value})
        else:
            pass
    final_list = list(letters_dict.items())
    sorted_list = sorted(final_list, key=second_element, reverse=True)
    final_dict = dict(sorted_list)

    print(f"--- Begin report of {file_path} ---")
    print(f"The book contains {len(words)} words \n")

    for key, value in final_dict.items():
        print(f"The letter {key} has appeared {value} times in the book")
