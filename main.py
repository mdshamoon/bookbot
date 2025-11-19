from stats import get_words_count, get_characters_count, get_sorted_list
import sys




def main():

    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        with open(book_path) as file:
            content = file.read()
            num_words = get_words_count(content)
            character_counts = get_characters_count(content)
            sorted_list = get_sorted_list(character_counts)
            print("============ BOOKBOT ============")
            print("Analyzing book found at books/frankenstein.txt...")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")

            for item in sorted_list:
                print(f"{item['char']}: {item['num']}")

            print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

main()