import requests

respons = requests.get(url="http://api.open-notify.org/iss-now.json")

print(respons)