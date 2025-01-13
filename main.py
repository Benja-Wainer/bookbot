def main():
    book_file = "books/frankenstein.txt"
    text = get_text(book_file)
    print(text)

def get_text(book_file):
    with open(book_file) as f:
        text = f.read()
        return text

main()
