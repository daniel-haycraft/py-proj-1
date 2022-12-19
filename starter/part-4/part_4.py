### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def inputs():
#     input("name of title")
#     input("author of said book")
#     input("your rating")
#     input("how many pages")
#     input("price with no $")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

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
    print(book_dictionary)
### Step 3 - Error handling 
## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

### Step 4 - if/elif/else
my_favs = ["ready player one", "the messenger", "Harry Potter", "The Hungry Game"]
my_favs= [title.upper() for title in my_favs]

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.
def main_menu():
    while True:
        print('hello welcome to daniels perfect book library!')
        print('you can see my books or create a book for me to check out!')
        try:
            main = int(input("enter 1: for create a book or enter 2 for access to my favorite books "))
        except:
            main = int(input("enter 1: for create a book or enter 2 for access to my favorite books "))
        if main == 1:
            inputs()
        elif main == 2:
            print(my_favs)
        else: 
            main_menu()
# Code here
main_menu()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
