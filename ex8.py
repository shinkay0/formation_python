import requests
from bs4 import BeautifulSoup

def get_element_or_default(element, div, class_name, default=""):
  try:
    return element.find(div, class_=class_name).text
  except AttributeError as e:
    print(e)

  return default

URL = "https://quotes.toscrape.com/"

try:
  res = requests.get(URL)
except requests.exceptions.RequestException as e:
  print(e)
  exit(1)

if res.status_code != 200:
  print("Connexion impossible")
  exit(1)
else:
  soup = BeautifulSoup(res.content, "html.parser")
  quotes = soup.find_all("div", class_="quote")

  print(len(quotes))
  
  for quote in quotes:
    text = get_element_or_default(quote, "span", "text", "Le texte n'existe pas")
    author = get_element_or_default(quote, "small", "author", "L'auteur n'existe pas")

    try:
      tags = quote.find("div", class_="tags")
      tags = tags.find_all("a")
    except AttributeError as e:
      print(e)
      tags = []

    print(f"Text: {text}")
    print(f"Author: {author}")
    print("tags:")
    for tag in tags:
      print(tag.text)
      
    print('-' * 15)
      
