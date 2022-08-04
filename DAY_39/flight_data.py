API_KEY = "yl353Isx-Ak4IUzytrljbRJ0X-C9OSbC"
TEQ_URL = "https://tequila-api.kiwi.com"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date,stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop = stop_overs
        self.via_city = via_city
