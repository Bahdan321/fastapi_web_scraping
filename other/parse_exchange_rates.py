import requests
from bs4 import BeautifulSoup

URL = "https://www.fontanka.ru/currency.html"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0", "accept": "*/*"}

def parse_exchange_rates():
    html = requests.get(URL, headers=HEADERS, params=None)
    soup = BeautifulSoup(html.text, "html.parser")
    if html.status_code == 200:
        #items = soup.find_all("table", class_="J-af9")
        items = soup.find_all("tbody", class_="J-agb")
        rates = []
        for i in items:
            rates.append({
                "str": i.find("td", class_="J-d3").get_text(),
                "val": i.find("td", class_="J-agl").get_text()
            })
        return(rates)
    else:
        return("Ошибка: " + str(html.status_code))