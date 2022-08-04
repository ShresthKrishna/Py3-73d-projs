import requests
SHEETY_ENDPOINT = "https://api.sheety.co/f5e2ce9e699734d114b89ab79e920c32/copyOfCopyOfFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}
    def get_place(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.data = self.response.json()
        return self.data

    def put_data(self, id, iata):
            new_data = {
                "price":
                    {
                        'iataCode': iata
                    }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{id}",
                json=new_data
            )
            return response.json()
