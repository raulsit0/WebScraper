import bs4
import requests

# url without page number
basic_url = ("http://books.toscrape.com/catalogue/page-{}.html")

# list of at least 4 star books
high_rated_titles = []

# iterate pages
for page in range(1,51):

    #create a soup on each page
    url_page = basic_url.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, "html.parser")

    #gathers all the date of the book
    books = soup.select(".product_pod")

    for book in books:


        # checks if they are 4 or 5 star books
        if len(book.select(".star-rating.Four")) != 0 or len(book.select(".star-rating.Five")) != 0:

            #store title in variable
            book_title = book.select("a")[1]["title"]

            #add book to list
            high_rated_titles.append(book_title)

for b in high_rated_titles:
    print(b)