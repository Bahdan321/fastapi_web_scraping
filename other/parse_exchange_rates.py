import requests
from bs4 import BeautifulSoup

def parse_exchange_rates():
    url = 'https://www.banki.ru/products/currency/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получаем курсы валют
    exchange_rates = soup.find_all('div', class_='currency-table__large-text')
    
    if len(exchange_rates) >= 3:  # Проверяем, что есть достаточно данных
        usd_rate = exchange_rates[0].text.strip()  # курс рубля к доллару
        eur_rate = exchange_rates[1].text.strip()  # курс рубля к евро
        btc_rate = exchange_rates[2].text.strip()  # курс рубля к биткоину

        return {
            'usd': usd_rate,
            'eur': eur_rate,
            'btc': btc_rate
        }
    else:
        return None  # В случае отсутствия данных возвращаем None

rates = parse_exchange_rates()
if rates:
    print(rates)
else:
    print("Failed to retrieve exchange rates. Please check the source or try again later.")