from requests import get
from bs4 import BeautifulSoup as bs

url = "https://www.drsquatch.com/"
soup = bs(get(url).text, "lxml")

final_links = []
final_cats = []

all_cats = soup.findAll('div', {"class": 'row py-6 mx-3'})
for cat in all_cats:
    # all_links = cat.find("ul").findChildren()
    all_links = cat.findAll("a")
    for link in all_links:
        cat_name = link.getText()
        # cat_link = link.findChild().get("href")
        cat_link = link.get("href").split('/')[-1]
        final_links.append(cat_link)
        final_cats.append(cat_name)

print(final_links, "\n\n")
print(final_cats)
