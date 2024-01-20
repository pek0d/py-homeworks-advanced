import json
import re

import requests
from bs4 import BeautifulSoup

# URL, который нужно запросить
url = "https://spb.hh.ru/search/vacancy?text=python+django+flask&area=1&area=2"

# Заголовки (Headers)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/91.0.4472.124 Safari/537.36"
}

# Отправка GET-запроса с использованием заголовков
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Находим все вакансии
    vacancies = soup.find_all("div", class_="vacancy-serp-item__layout")

    results = []
    for vacancy in vacancies:
        title = vacancy.find("span", class_="serp-item__title").text
        company = vacancy.find("a", {"data-qa": "vacancy-serp__vacancy-employer"}).text
        address = vacancy.find("div", {"data-qa": "vacancy-serp__vacancy-address"}).text
        city = address.split(",")[0]

        salary_element = (
            "span",
            {"data-qa": "vacancy-serp__vacancy-compensation"},
        )
        salary = salary_element.text if salary_element else print("не указано")

        link = vacancy.find("a", class_="bloko-link")["href"]

        if re.search(r"\bUSD\b", str(salary)) or re.search(
            r"dollar", str(salary), re.IGNORECASE
        ):
            results.append(
                {
                    "title": title,
                    "company": company,
                    "city": city,
                    "salary": str(salary.text.strip()) if salary else None,
                    "link": link,
                }
            )

    with open("vacancies_filtered.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
