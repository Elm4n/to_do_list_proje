import requests
import bs4

url = "https://en.wikipedia.org/wiki/Marand"
target_class = "vector-header-container"

r = requests.get(url)
data = r.text

soup = bs4.BeautifulSoup(data, "html.parser")
page_title = soup.select("title")
print(page_title)

items = soup.select("div.vector-header-container")
print("items :", len(items))