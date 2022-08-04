import pprint

import  requests
import lxml
from bs4 import BeautifulSoup
response = requests.get("https://www.imdb.com/list/ls055592025/")
# print(response.text)
empire_page = response.text
soup = BeautifulSoup(empire_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="lister-item-header")
for movies in all_movies:
    print(movies.text)
