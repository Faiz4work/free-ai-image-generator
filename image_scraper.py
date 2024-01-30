import requests
from parsel import Selector
from PIL import Image
from io import BytesIO
import os
import re

number_of_images_to_scrape = 25

url = "https://playgroundai.com/search?q="
keywords = input("Enter your keyword: ")
url = url+keywords


res = requests.get(url)
text = Selector(text=str(res.content))
script = text.xpath("//script[@id='__NEXT_DATA__']/text()").get()

pattern = '"url":"(.*?)"'
url_list = re.findall(pattern, script)

if not os.path.exists(keywords):
    os.mkdir(keywords)

counter = 1
for u in url_list[:number_of_images_to_scrape]:
    res = requests.get(u)
    with Image.open(BytesIO(res.content)) as image:
        path = f"{keywords}/{counter}.png"
        image.save(path)
        counter += 1