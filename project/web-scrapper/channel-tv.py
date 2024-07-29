import requests
from bs4 import BeautifulSoup
# get url and pass it to html parser
url = "https://www.channelstv.com"
page = requests.get(url)
webpage = BeautifulSoup(page.content, "html.parser")

#print(webpage)

find_title = webpage.find("title")
print(find_title)