import requests
from bs4 import BeautifulSoup
# get url and pass it to html parser
url = "https://www.appclick.ng"
page = requests.get(url)
webpage = BeautifulSoup(page.content, "html.parser")

# Find all elements with class "client-img"
all_images = webpage.find("div", class_="testimonial-slider-one")

testimonials = all_images.find_all("div", attrs={"class": "testimonial-item"})

for testimonial in testimonials:
    image = testimonial.find("img")
    image_src = image.attrs["src"]
    name = testimonial.find("h5")
    paragraph = testimonial.find("p")
    print(name.text, image_src, name.text)
  

    