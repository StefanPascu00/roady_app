import json

import requests
from bs4 import BeautifulSoup


class Gas:

    def __init__(self, path="config.json"):
        with open(path, "r") as f:
            config = json.loads(f.read())

        self.dict_prices = self.get_html_for_gas(config.get("gas_url"))
        self.avg_prices = self.calculate_avg()

    def get_html_for_gas(self, url, search_for="box_pret"):
        try:
            html_text = ""
            response = requests.get(url)

            if response.status_code == 200:
                html_text = response.text

            gas_prices_soup = BeautifulSoup(markup=html_text, features="html.parser")
            dates = gas_prices_soup.find_all("div", {"class": "location"})
            dates = [item.text for item in dates]
            prices = gas_prices_soup.find_all(id=search_for)
            prices = [price.text for price in prices]

            price_dict = dict(zip(dates, prices))

            return price_dict
        except Exception as e:
            print(f"Exception on getting gas prices {e}")

    def calculate_avg(self):
        prices = self.dict_prices.values()
        prices = [float(price.split(" ")[0]) for price in prices]
        return sum(prices) / len(prices)


if __name__ == '__main__':
    gas = Gas()
    print(gas.dict_prices)
    print(gas.avg_prices)
