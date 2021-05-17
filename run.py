import requests
from bs4 import BeautifulSoup
import os


def image_down(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    images = soup.find_all('a', {'class': 'internal'})
    for image in images:
        name = image['title'].replace('.png', '')
        link = image['href']
        with open(name + '.png', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)
image_down('https://commons.wikimedia.org/wiki/Commons:Stroke_Order_Project/Hiragana', 'hiragana')