def main():
    book_file = "books/frankenstein.txt"
    text = get_text(book_file)
    word_count = count_words(text)
    char_count = count_characters(text)
    # print(text)
    # print(f"The books has {word_count} words.")
    print("Character count:")
    for char in char_count:
        print(f"{char} appears {char_count[char]} times.")

def get_text(book_file):
    with open(book_file) as f:
        text = f.read()
        return text

def count_words(text):
    splitted_text = text.split()
    return len(splitted_text)

def count_characters(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

main()
