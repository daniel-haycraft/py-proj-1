my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}


# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def enter_book(book):
    result = f'the book of the year: {book["title"]} author: {book["author"]}, the year: {book["year"]}, the rating: {book["rating"]}, page count: {book["pages"]} '
    print(result)


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def title(book):
    result = f' {book["title"]}'
    print(result)



enter_book(my_book)
title(my_book)


# Finally, create at least three new functions that might be useful as we expand our home library app. 
# Perhaps thing of a way you could accept additional arguments when the function is called? 
# Also, imagine you have a list filled with dictionaries like above.

def change_book(title, author, year, rating, pages):
    my_book["title"] = title
    my_book["author"] = author
    my_book["year"] = year
    my_book["rating"] = rating
    my_book["pages"] = pages

change_book("Ready Player One", "Ernest", 1988, 10, 389)
# print(my_book)

books = []
def book_list(book):
    books.append(book)

book2 = {"title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}
book_list(my_book)
book_list(book2)
# print(books)
#specifically for testing


sorted(books, key=lambda i: i['author'])
