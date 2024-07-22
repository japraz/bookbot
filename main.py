def main():
    path = "/root/workspace/github.com/japraz/bookbot/books/frankenstein.txt"
    book_contents = book_text(path)
    num_words = count_words(book_contents)
    num_letters = count_letters(book_contents)
    dict = dict_to_list(num_letters)
    print(f"--- Begin report of books/frankenstein.txt ---\n {num_words} words found in the document")
    for i in dict:
        let = i["letter"]
        num = i["number"]
        print(f"The '{let}' character was found {num} times")
    
    
    
def sort_on(dict):
    return dict["number"]

def dict_to_list(num_letters):
    lister=[]
    for i in num_letters:
        lister.append({"letter" : i, "number" : num_letters[i] })
    lister.sort(reverse=True, key=sort_on)
    return lister 
    
def count_letters(book_contents):
    book_contents_lowered = book_contents.lower()
    letters_count = {}
    for letter in book_contents_lowered: 
        if letter in book_contents_lowered:
            if letter in letters_count and letter.isalpha():
                letters_count[letter] += 1 
            if letter not in letters_count and letter.isalpha():
                letters_count[letter] = 0
    return letters_count



def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def book_text(path):  
    with open(path) as f:
        return f.read()  


        
main()
