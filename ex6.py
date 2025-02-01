from bs4 import BeautifulSoup
import requests

URL = "https://books.toscrape.com/catalogue/category/books_1/index.html"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.content, "html.parser")
  
  books = soup.find_all("article", class_="product_pod")

  for book in books:
    title=book.find("h3").find("a")["title"]
    price=book.find("p", "price_color").text
    note = book.find("p", "star-rating")["class"][-1]
    available =  book.find("p", "instock")["class"][0]
    print()
    print(f"titre = {title}")
    print(f"prix = {price}")
    print(f"note = {note}")
    if available == 'instock':
      print("Le livre est disponible")
    else:
      print("Le livre n'est pas disponible")
else:
  print("Connexion impossible")
