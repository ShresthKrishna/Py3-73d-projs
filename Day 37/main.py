import requests
from datetime import datetime
TOKEN = "tokenvalue"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": "tokenvalue",
    "username": "shresthkrishna",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)
graph_endpoint = "https://pixe.la/v1/users/shresthkrishna/graphs"
graph_update = "https://pixe.la/v1/users/shresthkrishna/graphs/graph2"
# graph_params = {
#     "id": "graph1",
#     "name": "cycling graph",
#     "unit": "km",
#     "type": "float",
#     "color": "shibafu",
#     "date": "20210625"
#     "quantity": "5"
#
# }

today = datetime.now()
graph_params = {
    "id": "graph2",
    "name": "Study graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",


}
data = {
    "date": f"{today.strftime('%Y%m%d')}",
    "quantity": input("How many hours?"),

}

new_graph = {
    "name": "Study graph 02",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"

}
headers = {
    "X-USER-TOKEN": TOKEN
}
#To update the details of the graph
# response = requests.put(url=graph_update, json=new_graph, headers=headers)
# print(response.text)
#==============================================================================

# To update the value of pixel
# new_value = {
#     "quantity": "20",
# }
# update_url = f"{graph_update}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_url, json=new_value, headers=headers)
# print(response.text)
# =================================================================================

# To delete a pixel
# update_url = f"{graph_update}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=update_url, headers=headers)
# print(response.text)

#Data from user
update_url = f"{graph_update}/{today.strftime('%Y%m%d')}"
response = requests.put(url=update_url, json=data, headers=headers)
print(response.text)



