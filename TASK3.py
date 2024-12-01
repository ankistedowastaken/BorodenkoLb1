import requests
import datetime
import matplotlib.pyplot as plt

dates = []
rates = []


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


filtered_data = [item for item in data if 10 < item['rate'] < 100]


dates = [item['exchangedate'] for item in filtered_data]
rates = [item['rate'] for item in filtered_data]


dates.reverse()
rates.reverse()


plt.figure(figsize=(12, 6))
plt.plot(dates, rates, marker='o', markersize=8, linestyle='-', color='dodgerblue', alpha=0.8, label='Курс')
plt.fill_between(dates, rates, color='lightblue', alpha=0.3)  # Додаткове заповнення для акценту


plt.title("Динаміка курсу валют", fontsize=16, fontweight='bold')
plt.xlabel("Дата", fontsize=14)
plt.ylabel("Курс (UAH)", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(min(rates) - 1, max(rates) + 1)  # Межі Y для покращеної візуалізації
plt.grid(True, linestyle='--', alpha=0.6)


plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()


plt.show()