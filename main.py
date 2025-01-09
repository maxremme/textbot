from collections import Counter

def load_book():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    return text
    

def count_words(file):
    words = file.split()
    return len(words)

def count_char(file):
    c = Counter(file.lower()) 
    for item, value in c.most_common():
        if item.isalpha():
            print(f"The Character '{item}' was found {value} times.")

def main():
    book = load_book()
    print(f"\n----Begin Report----\n\nNumber of Words: {count_words(book)}\n")
    count_char(book)
    print(f"\n----End Report----\n")


if __name__ == "__main__":
    main()


