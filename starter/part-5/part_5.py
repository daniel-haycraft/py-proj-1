
### Step 1 - Store data in a .txt
import time

books = [{
    "title": "The Alchemist", 
    "author": "Paul Coelho", 
    "year": 1998, 
    "rating": 10, 
    "pages":389, 
    "price":17
    },
    {"title": "Hunger Games", 
    "author": "Collins", 
    "year": 2008, 
    "rating": 10,
    "pages":489, 
    "price":16
    },
    ]

with open("library.txt", "w") as f:
    f.write("The Alchemist, Paul Coelho, 1998, 10, 389, 17\n")
    f.write("The Hungry Games, Collins, 2008, 10, 400, 18\n")


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
    books.append(book_dictionary)
    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}, {price} \n")
        print(book_dictionary)
    time.sleep(4)


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
        print(books)
        time.sleep(10)
            



### Step 3 - if __name__ == "__main__":


## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

def main_menu():
        chicken = True
        while chicken:
            print('Hello and welcome to Daniels perfect library!')
            printer =  print("Enter 1 for create a book\nEnter 2 for access to my favorite books\nEnter 3 to create a list of your own favorite books!\nEnter 4 to select a specific book!\nEnter 5 to get the average ratings!\nEnter 6 to say good-bye")
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
            elif main == 4:
                get_book()
            elif main == 5:
                get_avg_rating()
            elif main == 6:
                chicken = False
                print('okay bye!')
            else:
                main_menu()
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
    with open("users.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}, {price} \n")
        print(book_dictionary)
        print('...initializing book')
        time.sleep(4)

def get_book():
    with open("library.txt", "r") as f:
        file = f.readlines()
    print(f'chose any number to get any book 0 of {len(file)}')
    try:
        index = int(input("find your book using numbers!\n"))
    except:
         index = int(input("find your book!"))
    index -= 1
    print(file[index])
    time.sleep(4)


def get_avg_rating():
    with open("library.txt", "r") as f:
        file = f.readlines()
    ratings = []
    for index in books:
        index = index["rating"]
        ratings.append(index)
    print("calculating...")
    time.sleep(2)
    print(sum(ratings)/len(file))
    time.sleep(3)
    

if __name__ == '__main__':
    main_menu()
