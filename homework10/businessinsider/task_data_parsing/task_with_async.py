"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и
проданы на уровне 52 Week High (справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом
максимуме за последний год.
"""

import asyncio
import datetime
import json
import re
from typing import Dict, List, Union

import aiohttp
from bs4 import BeautifulSoup


async def get_current_dollar_value() -> float:
    today = datetime.date.today().strftime("%d/%m/%Y")
    central_bank_url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={today}"
    dollar_value = (
        BeautifulSoup(await get_html_content(central_bank_url), "lxml")
        .find("valute", id="R01235")
        .find("value")
        .text.replace(",", ".")
    )
    return float(dollar_value)


def get_value_with_reg_exp(value, soup) -> Union[float, None]:
    pattern = r"([0-9]*\.[0-9]*)\r\n.*" + value
    request = re.findall(pattern, str(soup))
    if len(request) != 0:
        return float(request[0].replace(",", ""))


def get_potential_profit(soup) -> Union[float, None]:
    low52week_value = get_value_with_reg_exp(
        "52 Week Low", soup.find("div", {"class": "snapshot"})
    )
    high52week_value = get_value_with_reg_exp(
        "52 Week High", soup.find("div", {"class": "snapshot"})
    )
    if low52week_value and high52week_value:
        return round((high52week_value - low52week_value) / low52week_value * 100, 2)


async def get_html_content(url_: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url_) as response:
            return await response.text()


async def fetch_company_name_href_and_growth(url: str) -> List[Dict]:
    company_name_href_growth = []
    data_from_all_companies_page = (
        BeautifulSoup(await get_html_content(url), "lxml")
        .find_all("table")[1]
        .find_all("tr")[1:]
    )
    for company_info in data_from_all_companies_page:
        name = company_info.find_all("a")[0].text
        href = company_info.find_all("a")[0].get("href")
        growth = float(
            company_info.find_all("td")[9]
            .find_all("span")[1]
            .text.replace("%", "")
            .replace("%", "")
        )
        company_name_href_growth.append({"name": name, "href": href, "growth": growth})
    return company_name_href_growth


async def get_company_full_info(company_name_href_growth, current_dollar_value) -> Dict:
    base_url = "https://markets.businessinsider.com"
    company_url = base_url + company_name_href_growth["href"]
    soup = BeautifulSoup(await get_html_content(company_url), "lxml")
    price_in_dollars = soup.find(class_="price-section__current-value").text.replace(
        ",", ""
    )
    one_company_full_data = {
        "name": company_name_href_growth["name"],
        "code": soup.find(class_="price-section__category").find("span").text[2:],
        "price": round(float(price_in_dollars) * current_dollar_value, 2),
        "p_e_ratio": get_value_with_reg_exp(
            "P/E Ratio", soup.find_all("div", class_="snapshot__data-item")
        ),
        "growth": company_name_href_growth["growth"],
        "potential_profit": get_potential_profit(soup),
    }
    print(one_company_full_data)
    return one_company_full_data


def ten_most_expensive(data):
    sorted_data = sorted(data, key=lambda x: x["price"], reverse=True)[:10]
    save_data_in_json(sorted_data, "largest", key="price")


def ten_lowest_p_e_ratio(data):
    sorted_data = sorted(
        filter(lambda d: d["p_e_ratio"], data),
        key=lambda x: x["p_e_ratio"],
        reverse=False,
    )[:10]
    save_data_in_json(sorted_data, "smallest", key="p_e_ratio")


def ten_largest_growth(data):
    sorted_data = sorted(data, key=lambda x: x["growth"], reverse=True)[:10]
    save_data_in_json(sorted_data, "largest", key="growth")


def ten_largest_potential_profit(data):
    sorted_data = sorted(
        filter(lambda d: d["potential_profit"], data),
        key=lambda x: x["potential_profit"],
        reverse=True,
    )[:10]
    save_data_in_json(sorted_data, "largest", key="potential_profit")


def save_data_in_json(sorted_data: List[Dict], description: str, key: str):
    data_to_json_file = [
        {"code": company["code"], "name": company["name"], f"{key}": company[key]}
        for company in sorted_data
    ]
    json_file_name = "ten_companies_with_" + description + "_" + key + ".json"
    with open(json_file_name, "w") as file:
        file.write(json.dumps(data_to_json_file, indent=4))


async def main():
    url_start = "https://markets.businessinsider.com/index/components/s&p_500?p="
    ten_pages = [url_start + str(value) for value in range(1, 11)]
    tasks_1 = [
        asyncio.create_task(fetch_company_name_href_and_growth(url))
        for url in ten_pages
    ]
    data_from_all_pages = await asyncio.gather(*tasks_1)
    current_dollar_value = await get_current_dollar_value()
    tasks_2 = [
        asyncio.create_task(get_company_full_info(company, current_dollar_value))
        for data_from_one_page in data_from_all_pages
        for company in data_from_one_page
    ]
    return await asyncio.gather(*tasks_2)


if __name__ == "__main__":
    companies_data = asyncio.run(main())
    ten_most_expensive(companies_data)
    ten_lowest_p_e_ratio(companies_data)
    ten_largest_growth(companies_data)
    ten_largest_potential_profit(companies_data)
