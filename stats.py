def count_words(text):
    words = text.split()
    word_length = len(words)
    return word_length

def number_of_characters(text):
    new_dict = {}
    words = text.split()
    for word in words:
        lower_case = word.lower()
        for letter in lower_case:
            if letter not in new_dict:
                new_dict[letter] = 1
            else:
                new_dict[letter] += 1
    return new_dict
                    
def sort_characters(new_dict):

    new_list = []
    for key, value in dict.items(new_dict): 
        new_dict = {"char": key, "num": value}
        new_list.append(new_dict)
        new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(items):
    return items["num"]


    # car["color"] = "blue"