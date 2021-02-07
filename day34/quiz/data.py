import requests


parameters = {"amount": 10, "type": "boolean"}
url = "https://opentdb.com/api.php"
response = requests.get(url=url, params=parameters)

question_data = response.json()["results"]
