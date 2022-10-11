import requests

BASE_URL = "http://127.0.0.1:5000"
TOKEN = "ABCDEFGH12345678"
CONTENT_TYPE = "application/json"

MAX = 1000000000

class RequestsSender:
    def __init__(self, base_url, token, content_type):
        self.base_url = base_url
        self.token = token
        self.content_type = content_type
    
    def get_url(self, route):
        return BASE_URL + route if route[0] == "/" else BASE_URL + "/" + route

    def get(self, route):
        res = requests.get(
            self.get_url(route),
            headers = {
                'Content-Type': self.content_type,
                'Access-Token': self.token
            }
        )
        return res.json()

    def post(self, route, auth_key, value):
        res = requests.post(
            self.get_url(route),
            headers = {
                'Content-Type': self.content_type,
                'Access-Token': self.token
            },
            json = {
                'auth_key': auth_key,
                'value': value
            }
        )
        return res.json()

def get_auth_key():
    return sender.get(
        "/start"
    )['auth_key']

def get_result(auth_key, value):
    return sender.post(
        "/query",
        auth_key,
        value
    )['result']

def start():
    auth_key = get_auth_key()

    # Binary search
    l, r = 0, MAX
    while l <= r:
        m = (l + r) // 2
        result = get_result(auth_key, m)

        if result == 'up':
            l = m + 1
        elif result == 'down':
            r = m - 1
        elif result == 'fail':
            # LOSE
            print("YOU LOSE!")
            break
        else:
            # WIN
            print("YOU WON!")
            print(f"The answer is {m}")
            break

if __name__ == '__main__':
    sender = RequestsSender(BASE_URL, TOKEN, CONTENT_TYPE)
    start()