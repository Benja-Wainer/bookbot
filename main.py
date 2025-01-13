def main():
    book_file = "books/frankenstein.txt"
    text = get_text(book_file)
    word_count = count_words(text)
    char_count = count_characters(text)
    # print(text)
    # print(f"The books has {word_count} words.")
    char_count.sort(key=sort_on_character)
    print(char_count)

def get_text(book_file):
    with open(book_file) as f:
        text = f.read()
        return text

def count_words(text):
    splitted_text = text.split()
    return len(splitted_text)

def count_characters(text):
    character_count = {}
    count_list = []
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        elif char.isalpha():
            character_count[char] = 1
    for char in character_count:
        count_list.append({"character": char, "times": character_count[char]})
    return count_list

def sort_on_character(dict):
    return dict["character"]

main()
