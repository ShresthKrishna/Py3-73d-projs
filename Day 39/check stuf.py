import requests
from pprint import pprint
# KIWI_API_KEY = "yl353Isx-Ak4IUzytrljbRJ0X-C9OSbC"
# KIWI_URL = "https://tequila-api.kiwi.com/locations/query"
#
# data = {
#     "term": "paris",
#     "location_types": "city"
# }
# header = {
#     "apikey": KIWI_API_KEY
#
# }
# response = requests.get(url=KIWI_URL, params= data, headers=header)
# pprint(response.json()["locations"])
sheety = "https://api.sheety.co/70dd7c7ed02c78186d7034a1219a927f/copyOfFlightDeals/prices/Paris"
# response = requests.put(sheety).json()
header = {
    "Content-Type":"application/json"
}
body={"prices": {
    "iataCode": "hello"
  }


}
requests.put(sheety,json=body,headers=header)

