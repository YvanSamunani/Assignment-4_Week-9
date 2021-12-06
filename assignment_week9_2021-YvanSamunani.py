import requests
from bs4 import BeautifulSoup

book_prices = []
page = requests.get('https://www.amazon.com/Best-Sellers-Books/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1')

print(page)
soup = BeautifulSoup(page.content, 'lxml')
best_sellers = soup.find_all(class_='a-size-base a-color-price')


for books in best_sellers:
    new_string = float(books.text.replace("$", ""))
    print(new_string)
    book_prices.append(new_string)

book_prices.sort(reverse=True)
print(book_prices)



# # print(soup.prettify())


