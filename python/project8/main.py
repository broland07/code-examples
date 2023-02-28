import requests

respons = requests.get(url="http://api.open-notify.org/iss-now.json")
respons.raise_for_status()

data = respons.json()["iss_position"]
print(data)