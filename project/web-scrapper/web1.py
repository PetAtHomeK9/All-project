import requests
from bs4 import BeautifulSoup

target = requests.get("https://www.appclick.ng")

soup = BeautifulSoup(target.content, "html.parser")

WGS = soup.find("div", attrs={"c" : "accordionExample"})

faq1_div = WGS.find_all("div", attrs={"class" : "client-name"})

for image in WGS:
    question = image.find("button", attrs={})

print(faq1_div)
