import requests
from pprint import pprint
from flight_data import FlightData
API_KEY = "yl353Isx-Ak4IUzytrljbRJ0X-C9OSbC"
TEQ_URL = "https://tequila-api.kiwi.com"
class FlightSearch:
    def get_dest(self, city):
        self.city = city
        self.api = API_KEY
        self.header = {
            "apikey": API_KEY
        }
        body = {
            "term":f"{city}",
            "location_types": "city"
        }
        self.response = requests.get(
            url=f"{TEQ_URL}/locations/query",
            params=body,
            headers=self.header
        )
        self.data=self.response.json()["locations"][0]['code']
        return self.data
    def flight(self, fly_from, fly_to,date_from, date_to):
        query = {
            "fly_from": f"{fly_from}",
            "fly_to": f"{fly_to}",
            "date_from ": f"{date_from}",
            "date_to": f"{date_to}",
            "nights_in_dst_from" : f"{7}",
            "nights_in_dst_to": f"{28}",
            "flight_type": "round",
            "curr": f"GBP",
            "max_stopovers": 0
        }
        self.header = {
            "apikey": API_KEY
        }
        search_url = f"{TEQ_URL}/v2/search"
        response = requests.get(url=search_url, params= query, headers=self.header)
        try:
            data = response.json()["data"][0]
        except IndexError:

            query["max_stopovers"] = 1
            response = requests.get(url=search_url, params=query, headers=self.header)
            data = response.json()["data"][0]
            return None

        flight = FlightData(
            price=data["price"],
            destination_city=data["cityTo"],
            destination_airport=data["cityCodeTo"],
            origin_city=data["cityFrom"],
            origin_airport=data["cityCodeFrom"],
            out_date=data["route"][0]['local_arrival'].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],

        )
        print(f"{flight.destination_city}: {flight.price}")
        return flight

# flight = FlightSearch()
# print(flight.flight(date_from="29/06/2021",date_to="29/12/2021", fly_from="LON", fly_to="PAR", currency="INR"))




