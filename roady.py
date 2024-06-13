# benzina sau motorina
# oras plecare , sosire
# numar de persoane
# consum
import json
from distance import Distance
from gas_price import Gas


class Roady:

    def __init__(self, departure_city: str, destination_city: str, number_of_person: int, fuel_usage: float,
                 fuel: str = "benzina", path: str = "config.json"):
        with open(path, "r") as f:
            config = json.loads(f.read())

        self.distance = Distance(departure_city, destination_city, config)
        self.gas = Gas(config, fuel)
        self.number_of_person = number_of_person
        self.fuel_usage = fuel_usage

    def calculate_price_per_person(self):
        km = float(self.distance.km.split(" ")[0])
        total_liters = self.fuel_usage * km / 100
        total_price = self.gas.avg_prices * total_liters
        return total_price / self.number_of_person


if __name__ == '__main__':
    roady = Roady("Bucuresti", "Iasi", 3, 10.0)
    print(roady.calculate_price_per_person())
