# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)
## TOO MUCH WORK WITHOUT PANDA!!!
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temprature.append(int(row[1]))
# print(temprature)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print("\n\n\n\n")
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print("\n\n\n\n")
# print(data_list)
# print("\n\n\n\n")
#
# # print(f" AVG TEMP: {round(sum(data_list)/len(data_list),2)}")
# print(data["temp"].max())
# print("\n\n\n\n")
#
# # get data in column
# print(data["condition"])
# print("\n\n\n\n")
# print(data.condition)

# get data in rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
mon_temp = data.temp[data.day == 'Monday']
print(f"{int(mon_temp * 1.8 + 32)} F")

# Create a Dataframe from scratch

data_dict={
    "students": ["amy", "mamy", "amymamy"],
    "score":[76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv('examplecsv.csv')
print(data)