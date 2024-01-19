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
        title = vacancy.find("span", class_="serp-item__title")
        company = vacancy.find("a", class_="bloko-link bloko-link_kind-tertiary")[
            "href"
        ]
        city = vacancy.find("div", class_="vacancy-serp__vacancy-address")
        salary = vacancy.find("span", class_="vacancy-serp-item__compensation")
        vacancy_link = vacancy.find("a", class_="oko-link")
        description = vacancy.find("div", class_="g-user-content")

        if re.search(r"\bUSD\b", str(salary)) or re.search(
            r"dollar", str(salary), re.IGNORECASE
        ):
            results.append(
                {
                    "title": title,
                    "company": company,
                    "city": city,
                    "salary": str(salary.text.strip()) if salary else None,
                    "link": vacancy_link,
                }
            )

    with open("vacancies_filtered.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
