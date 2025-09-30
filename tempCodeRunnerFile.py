import requests
import bs4

url = "http://books.toscrape.com/"
target_class = "product_pod"

r = requests.get(url)
data = r.text
soup = bs4.BeautifulSoup(data, "html.parser")

title = soup.select("title")
print(title)