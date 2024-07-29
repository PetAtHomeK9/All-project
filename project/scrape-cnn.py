import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://coinmarketcap.com"

coinmarketcap = requests.get(url)
whole_link = BeautifulSoup(coinmarketcap.content, "html.parser")
slink = whole_link.find_all("div", class_= {"sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl"})
text = whole_link.get_text()

print(slink)