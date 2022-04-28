import requests
import time

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating a User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": "workout1",
    "name": "Workout Graph",
    "unit": "Calories",
    "type": "int",
    "color": "ajisai",
}

# Creating a Graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

graph_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"

date = time.strftime("%Y%m%d")
graph_pixel_params = {
    "date": f"{date}",
    "quantity": "1250",
}

# Adding pixel to the Graph
# response = requests.post(url=graph_pixel_endpoint, json=graph_pixel_params, headers=headers)
# print(response.text)

graph_pixel_date_endpoint = f"{graph_pixel_endpoint}/{date}"
graph_pixel_date_params = {
    "quantity": "500",
}

# Updating a pixel on the graph
# response = requests.put(url=graph_pixel_date_endpoint, json=graph_pixel_date_params, headers=headers)
# print(response.text)

# Deleting a pixel
response = requests.delete(url=graph_pixel_date_endpoint, headers=headers)
print(response.text)
