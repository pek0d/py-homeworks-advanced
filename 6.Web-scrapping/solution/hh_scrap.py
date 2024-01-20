import json
import re

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/91.0.4472.124 Safari/537.36"
}

for page in range(10):
    url = f"https://spb.hh.ru/search/vacancy?text=python+django+flask&area=1&area=2&page={page}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        vacancies = soup.find_all("div", class_="vacancy-serp-item__layout")

        results = []
        for vacancy in vacancies:
            company = vacancy.find(
                "a", {"data-qa": "vacancy-serp__vacancy-employer"}
            ).text
            address = vacancy.find(
                "div", {"data-qa": "vacancy-serp__vacancy-address"}
            ).text
            city = address.split(",")[0]

            salary_element = vacancy.find(
                "span",
                {"data-qa": "vacancy-serp__vacancy-compensation"},
            )
            salary = salary_element.text if salary_element else "Не указана"

            link = vacancy.find("a", class_="bloko-link")["href"]

            if re.search(r"\bUSD\b", str(salary)) or re.search(
                r"dollar", str(salary), re.IGNORECASE
            ):
                results.append(
                    {
                        "company": company,
                        "city": city,
                        "salary": salary,
                        "link": link,
                    }
                )

        with open("vacancies_filtered.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
