### Step 1 - Store data in a .txt
import time


with open("library.txt", "w") as f:
    f.write("The Alchemist, Paul Coelho, 1998, 10, 389, 17\n")

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def inputs():
    try:
        title  = str(input("name of title "))
    except:
        title = str(input("using words, please tell me a name of a great title "))
    try:
        author = str(input("author of said book "))
    except:
        author = input("author of said book ")
    try:
        year = int(input("year it was published "))
    except: 
        year = int(input("year in numbers it was published "))
    try:
        rating = float(input("your rating "))
    except:
        rating = float(input("just any number 1-10 including dec "))
    try:
        pages = int(input("how many pages "))
    except: 
        pages = int(input("try using whole number for pages "))
    try:
        price = float(input("price with no $ "))
    except: 
        price = float(input("using decimals is a great place to start, remember don't use $ "))
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages,
        "price": price
    }
    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}, {price} \n")
        print(book_dictionary)

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def open_my_books():
    with open("library.txt", "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages, price = line.split(", ")
            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages),
                "price": float(price)
            }
            print(book_dictionary)


### Step 3 - if __name__ == "__main__":


## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

def main_menu():
        while True:
            print('hello welcome to daniels perfect book library!')
            print('you can see my books or create a book for me to check out!')
            printer =  print("enter 1: for create a book\nenter 2 for access to my favorite books\nenter 3 to create a list of your favorite books!")
            try:
                main = int(input(""))
            except:
                main = int(input(printer))
            if main == 1:
                inputs()
            elif main == 2:
                open_my_books()
            elif main == 3:
                create_your_own()
            elif main == 94:
                print('you guessed the right number!')
# Code this at the bottom of the script



### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def create_your_own():
    try:
        title  = str(input("name of title "))
    except:
        title = str(input("using words, please tell me a name of a great title "))
    try:
        author = str(input("author of said book "))
    except:
        author = input("author of said book ")
    try:
        year = int(input("year it was published "))
    except: 
        year = int(input("year in numbers it was published "))
    try:
        rating = float(input("your rating "))
    except:
        rating = float(input("just any number 1-10 including dec "))
    try:
        pages = int(input("how many pages "))
    except: 
        pages = int(input("try using whole number for pages "))
    try:
        price = float(input("price with no $ "))
    except: 
        price = float(input("using decimals is a great place to start, remember don't use $ "))
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages,
        "price": price
    }
    with open("users.txt", "w") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}, {price} \n")
        print(book_dictionary)
        print('...initializing book')
        time.sleep(4)



if __name__ == '__main__':
    main_menu()