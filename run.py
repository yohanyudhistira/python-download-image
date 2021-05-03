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
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)
image_down('https://www.airbnb.co.uk/s/Ginza--Chuo--Tokyo--Japan/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Ginza%2C%20Chuo%2C%20Tokyo%2C%20Japan&place_id=ChIJu2-DAeeLGGARUZipC7OFRmA&source=structured_search_input_header&search_type=autocomplete_click', 'ginza')