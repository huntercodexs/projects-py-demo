import requests

URL = "https://www.mockaroo.com/"

def fetch_net():
    response = requests.get(URL)
    if response.status_code == 200:
        return "abc"
    return "bcd"

def parse():
    answer = fetch_net() + str(123)
    return answer

