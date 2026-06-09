import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"
response = requests.get(url, headers={"Accept-Encoding": "utf-8"})
soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])  # header row
    
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([title, price])

print("Done! Check books.csv")