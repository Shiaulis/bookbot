def main():
    book_path = "books/frankenstein.txt"
    content = get_file_content(book_path)
    print(content)

def get_file_content(path):
    with open(path) as file:
        return file.read()


main()
