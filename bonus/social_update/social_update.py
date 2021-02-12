import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://routergods.ryver.com/api/1/odata.svc"

headers = {"Accept": "application/json", "Content-Type": "application/json"}
auth = requests.auth.HTTPBasicAuth(
    os.getenv("RYVER_USER"), os.getenv("RYVER_PASSWORD")
)

# -- FIND FORUM ID -- #
# endpoint = "/forums"
# skip = 0

# for _ in range(10):
#     params = {"$select": "id,name", "$top": 50, "$skip": skip}
#     response = requests.get(
#         BASE_URL + endpoint, params=params, headers=headers, auth=auth
#     )
#     data = response.json()
#     for forum in data["d"]["results"]:
#         if "100days" in forum["name"].lower():
#             print(forum)
#     if len(data["d"]["results"]) < 50:
#         break
#     skip += 50

# 'id': 1364174, 'name': 'Dev-Python-100daysofcode'

parser = argparse.ArgumentParser(description="Social Media Poster")
parser.add_argument("-m", dest="message", type=str, help="")
parser.add_argument("-d", dest="day", type=int, help="day completed")

args = parser.parse_args()
if not args.day and not args.message:
    print("must pass either days, or message.  Can pass both")

message = ""

if args.day:
    message += f"I have completed day {args.day} of 100DaysofCode. "

if args.message:
    message += f"{args.message} "

if args.day:
    message += (
        "Today's code is posted to: "
        f"https://github.com/dpnetca/100daysOfCode/tree/master/day{args.day}"
    )


# endpoint = "/forums(id=1364174)/Chat.PostMessage()"
endpoint = "/users(id=1218139)/Chat.PostMessage()"

data = {"body": message}
response = requests.post(
    BASE_URL + endpoint, headers=headers, auth=auth, json=data
)
print(response.text)
