# WebScrapy
It provides the code to scrape from a books listing website, providing the title, price, rating of a book, along with whether it is still in stock and its url.\n

The code in this repository scrapes from: "http://books.toscrape.com/".\n
It then ingests the data into a MongoDB database hosted on localhost, port 27017, into a database called "books" and collection called "titles".\n

# Running
First, make sure MongoDB is running on port 27017, on localhost \n
Next, run scrapy crawl books from the scrapy project folder "books"\n
You can now confirm that the data was stored on MongoDB in books database using MongoDB Compass\n
