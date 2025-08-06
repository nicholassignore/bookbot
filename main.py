from stats import count_words, number_of_characters, sort_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

    

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    text_len = count_words(text)
    print(f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {text_len} total words
--------- Character Count -------''')
    number_of_characters(text)
    dictionary_of_chars_and_counts = number_of_characters(text)
    sortedDict = sort_characters(dictionary_of_chars_and_counts)
    for char_dict in sortedDict:
        character = char_dict["char"]  # Get the actual character
        count = char_dict["num"]       # Get the count
        if character.isalpha():
            # Print in the format: character: count
            print(f"{character}: {count}")
        else:
            continue
            # Skip this iteration
    print("============= END ===============")

    
            



    
main()


# Write a new function that accepts the text from the book as a string, and returns the number of words in the string. The .split() method will be helpful here.
# Instead of printing the books contents, print this message to the console:
# {num_words} words found in the document

# Replace {num_words} with the actual number of words in the book.