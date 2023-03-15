import requests
from bs4 import BeautifulSoup
import os

url = "https://www.avogado6.com"  # 将 example.com 替换成你要爬取的网站

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img")

if not os.path.exists("avogado6"):
    os.mkdir("avogado6")

for img_tag in img_tags:
    img_url = img_tag.get("src")
    # print(img_url)
    if img_url.startswith("http"):
        filename = os.path.basename(img_url)
        print(filename)
        r_filename = 'https://static.wixstatic.com/media/' + str(filename)
        img_response = requests.get(r_filename)
        # r_filename = 'https://static.wixstatic.com/media/' + filename
        # print(r_filename)。
        filename = './avogado6/' + str(filename)
        with open(filename, "wb") as f:
            f.write(img_response.content)
        print("Downloaded", filename)
