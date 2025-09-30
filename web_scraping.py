import requests
import bs4

url = "http://books.toscrape.com/"
target_class = "product_pod"

r = requests.get(url)
data = r.text

soup = bs4.BeautifulSoup(data, "html.parser")

title = soup.title.text
print(title)

items = soup.select("div.product_pod")
print(" items:", len(items))   #to check if it is empty or not

items = soup.find_all("div", class_= target_class )  #div's with "product_pod" class
titles = []
images = []
for item in items:    #for each div.product_pod
    book_title = item.h3.a["title"]  #first <a> in first h3 header
    titles.append(book_title)

    img_tag = item.find("img")  #first image tag in div
    img_url = img_tag["src"]    #book image link(src inside <img)
    img_url = url + img_url      #http://books.toscrape.com/media/cache/5e/7f/5e7f...jpg
    images.append(img_url)

print(titles)
print(images)