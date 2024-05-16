
def main():
    with open('books/frankenstein.txt', 'r') as file:
        lines = file.read()
        words = lines.split()
        length = len(words)

        print(length)


main()