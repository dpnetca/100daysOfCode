import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = "dpnetca"
GRAPH_ID = "graph1"
BASE_URL = "https://pixe.la/v1/users"

# CREATE USER
# user_url = "https://pixe.la/v1/users"

# user_data = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=user_url, json=user_data)
# print(response.text)
# {
# "message":
#   "Success. Let's visit https://pixe.la/@dpnetca , it is your profile page!",
# "isSuccess": true
# }

# CREATE GRAPH
# graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs"

# headers = {"X-USER-TOKEN": TOKEN}

# graph_data = {
#     "id": GRAPH_ID,
#     "name": "100DaysofCode",
#     "unit": "minutes",
#     "type": "int",
#     "color": "shibafu",
# }
# response = requests.post(url=graph_url, json=graph_data, headers=headers)
# print(response.text)


# POST PIXEL
# pixel_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# headers = {"X-USER-TOKEN": TOKEN}
# # now = datetime.now()
# now = datetime(year=2021, month=2, day=10)
# pixel_data = {
#     # "date": "20210211",
#     "date": now.strftime("%Y%m%d"),
#     "quantity": "120",
# }

# response = requests.post(url=pixel_url, json=pixel_data, headers=headers)
# print(response.text)

# PUT (update) PIXEL
# date = datetime(year=2021, month=2, day=10)
# date.strftime("%Y%m%d")

# pixel_url = (
#     f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
# )
# headers = {"X-USER-TOKEN": TOKEN}
# pixel_data = {
#     "quantity": "15",
# }

# response = requests.put(url=pixel_url, json=pixel_data, headers=headers)
# print(response.text)

# PUT (update)- increment PIXEL
# date = datetime(year=2021, month=2, day=10)
# date.strftime("%Y%m%d")

# pixel_url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/increment"
# headers = {"X-USER-TOKEN": TOKEN}

# response = requests.put(url=pixel_url, headers=headers)
# print(response.text)


# DELETE PIXEL
date = datetime(year=2021, month=2, day=10)
date.strftime("%Y%m%d")

pixel_url = (
    f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
)
headers = {"X-USER-TOKEN": TOKEN}

response = requests.delete(url=pixel_url, headers=headers)
print(response.text)
