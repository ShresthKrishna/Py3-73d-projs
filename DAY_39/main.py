#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime
from pprint import pprint
cur_date = datetime.datetime.now().date()
fly_tom = cur_date + datetime.timedelta(1)
fly_tom = fly_tom.strftime("%d/%m/%Y")
fly_month = cur_date + datetime.timedelta()
fly_month = fly_month.strftime("%d/%m/%Y")
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_place()
print(sheet_data)
# dep_city = "LON"
# for i in sheet_data:
#     if i['iataCode'] == '':
#         i['iataCode'] = flight_search.get_dest(i["city"])
#         # print(i)
#         data_manager.data = sheet_data
#         data_manager.put_data(i["id"], i["iataCode"])
#     else:
#             fly = flight_search.flight(date_from=fly_tom, date_to=fly_month,fly_from=dep_city, fly_to=i["iataCode"])
#             # print(fly.price)
#
#             if fly!= None and fly.price < i["lowestPrice"]:
#                 try:
#                     notification_manager.send_sms(message=f"Low price alert! Only £{fly.price} "
#                                 f"to fly from {fly.origin_city}-"
#                                 f"{fly.origin_airport} to "
#                                 f"{fly.destination_city}-"
#                                 f"{fly.destination_airport}, from "
#                                 f"{fly.out_date} to "
#                                 f"{fly.return_date}."
#                     )
#                 except AttributeError:
#                     pass