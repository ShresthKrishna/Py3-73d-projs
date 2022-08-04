from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
article = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)
    article_link = article_tag.get("href")
    article_links.append(article_link)
article_upvote = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvote = [int (item.split(" ")[0]) for item in article_upvote]
print(article_upvote)
print(article_upvote.index(max(article_upvote)))
print(article_links)














# import lxml
# file = open("website.html", mode='rb')
# content = file.read()
#
# # soup = BeautifulSoup(content, 'html.parser') might not work with certain sites
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.title)  #return title
# # print(soup.prettify())  #appends file properly
# # print(soup.a)   #return first link in the file
#
# soup_anchor = soup.find_all(name="a")
# # print(soup_anchor)
#
#
# for tag in soup_anchor:
#     print("=============")
#     print(tag.getText())
#     print("#")
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# # company_url = soup.select_one(selector="p a") # this is basically like in css selector as we want the href link which is between a and p tag
# company_url = soup.select_one(selector="#name") # this is basically like in css selector as we want the detail which is of id name
#
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)
#
# print("###############################################")

