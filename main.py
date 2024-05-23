def main():
    with (open('books/frankenstein.txt', 'r') as file):
        lines = file.read()
        #words = lines.split()
        lower_letters = lines.lower()
        counted_letters = {}

        for letter in lower_letters:
            if letter in counted_letters:
                counted_letters[letter]['num'] += 1
            else:
                counted_letters[letter] = {'name': letter, 'num': 1}
        print(counted_letters)
        counted_letters_list = list(counted_letters.values())

        def sort_on(dict):
            return dict["num"]

        counted_letters_list.sort(key=sort_on)

        print(
            f'''
--- Begin report of books/frankenstein.txt ---
{counted_letters} words found in the document
            '''
        )

        for letter in counted_letters_list:
            if letter["name"].isalpha():
                print(f' The {letter["name"]} character was found {letter["num"]} times')


        print(
            '''
            --- End report ---
            '''
        )
        #print(counted_letters_list)


main()