from bs4 import BeautifulSoup
import requests

URL = "https://www.allocine.fr/film/meilleurs/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.content, "html.parser")
  
  movies = soup.find_all("li", class_="mdl")

  with open("movies.csv", "w", newline="") as f:
    for movie in movies:
      title = movie.h2.a.text
      note = movie.find("span", "stareval-note").text
      author = movie.find("div", class_="meta-body-item meta-body-direction")
      author = author.find_all("span")[1].text

      f.write(f"{title};{note};{author}\n")