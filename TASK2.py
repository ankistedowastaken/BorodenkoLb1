import requests
import datetime

today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).strftime('%Y%m%d')
end_date = (today - datetime.timedelta(days=1)).strftime('%Y%m%d')

url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&sort=exchangedate&order=desc&json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data:
        print(f"Дата: {item['exchangedate']}, Валюта: {item['cc']}, Курс: {item['rate']}")
else:
    print(f"Помилка: {response.status_code}")