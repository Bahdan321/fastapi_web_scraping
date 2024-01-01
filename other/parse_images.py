import requests
from bs4 import BeautifulSoup

def parse_images(query):
    url = f'https://www.google.com/search?q={query}&tbm=isch'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img', class_='t0fcAb')
    images = [tag['src'] for tag in image_tags][:10]
    return images

query = 'котенок'
images = parse_images(query)
print(images)