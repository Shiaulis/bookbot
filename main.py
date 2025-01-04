def main():
    book_path = "books/frankenstein.txt"
    content = get_file_content(book_path)

    print("--- Begin report of books/frankenstein.txt ---")

    word_count = get_word_count(content)
    print(f"{word_count} words found in the document")
    print()

    character_stats = get_character_stats(content)
    print_character_stats(character_stats)

    print("--- End report ---")

def get_file_content(path):
    with open(path) as file:
        return file.read()

def get_word_count(content):
    words = content.split()
    return len(words)

def get_character_stats(content):
    lowercased_content = content.lower()

    characters = {}
    for character in lowercased_content:
        if character in characters: 
            characters[character] += 1
        else:
            characters[character] = 1

    return characters

def print_character_stats(character_stats):
    stat_list = convert_dictionary_to_list(character_stats)
    stat_list.sort(reverse=True, key=sort_on)
    for item in stat_list:
        letter = item["letter"]
        stat = item["stat"]
        if letter.isalpha():
            print(f"The '{letter}' character was found {stat} times")

def convert_dictionary_to_list(dictionary):
    list = []
    for key in dictionary:
        list.append({"letter": key, "stat": dictionary[key]})
    return list

def sort_on(dictionary):
    return dictionary["stat"]


main()
