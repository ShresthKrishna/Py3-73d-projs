import csv
import prettify
import pprint

with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
for i in list_of_rows:
    for j in i:
        print(j)