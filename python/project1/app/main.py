import requests
from bs4 import BeautifulSoup
import json
import random
import requests

response = requests.get("https://www.napiarfolyam.hu/%C3%A1rfolyam/OTP+Bank/deviza%C3%A1rfolyamok/")
soup = BeautifulSoup(response.content, 'html.parser')
field_eur = soup.find_all('td')[32].get_text()
daily_eur = str(field_eur).split('.')[0]

def final(x, y):
    return y / x
    
daily_max = str(final(int(daily_eur), 100000)).split('.')[0]

if __name__ == '__main__':
    url = "SLACK_URL"
    message = ("Daily: " + daily_eur + " - 100K: " + daily_max + " €")
    title = (f"Daily OTP HUF-EUR :zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":moneybag:",
        #"channel" : "#home-lab",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    
    headers = {'Content-Type': "application/json", 'Content-Length': "daily_eur"}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)