def main():
    book_file = "books/frankenstein.txt"
    text = get_text(book_file)
    word_count = count_words(text)
    # print(text)
    print(f"The books has {word_count} words.")

def get_text(book_file):
    with open(book_file) as f:
        text = f.read()
        return text

def count_words(text):
    splitted_text = text.split()
    return len(splitted_text)

main()
