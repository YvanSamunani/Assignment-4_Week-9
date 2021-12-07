import pandas as pd
import requests
from bs4 import BeautifulSoup

# Request the amazon url
page = requests.get('https://www.amazon.com/Best-Sellers-Books/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1')

print(page)

# Create a BeautifulSoup object to make web scraping easier and use 'html.parser' so that it knows it's an html page

soup = BeautifulSoup(page.content, 'html.parser')

# Accessing the main class with all books
best_sellers = soup.find(class_='p13n-gridRow')

# Accessing the class in all books divisions with book names, reviews and prices
books = best_sellers.find_all(class_='zg-grid-general-faceout')

# Accessing names of all the books and adding them in book_names list
book_names= [books.find(class_='_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y').get_text() for book in books]

# Accessing book reviews of all the books and adding them in book_reviews list
book_reviews = [books.find(class_='a-size-small').get_text() for book in books]

# Accessing prices of all the books and adding them in book_price list
book_price = [books.find(class_='_p13n-zg-list-grid-desktop_price_p13n-sc-price__3mJ9Z').get_text() for book in books]

# Changing the price datatype from str to float and removing the $ sign
book_price = float (book_price.replace("$", ""))

# Using pandas to present the output in a table
books_table = pd.DataFrame(
    {
        'Names': book_names,
        'Reviews': book_reviews,
        'Prices' : book_price
    })

# Sorting the prices in a descending order
books_table.sort_values("Prices", axis= 0, ascending = True, inplace = True, na_position = 'last')

# Printing the table with book names, reviews and their prices.
print(books_table)
