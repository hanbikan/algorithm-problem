import requests

BASE_URL = "http://127.0.0.1:5000"
TOKEN = "ABCDEFGH12345678"
CONTENT_TYPE = "application/json"

BLANK, ME, CP = 0, 1, 2

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

    def post(self, route, json):
        res = requests.post(
            self.get_url(route),
            headers = {
                'Content-Type': self.content_type,
                'Access-Token': self.token
            },
            json = json
        )
        return res.json()

def get_started():
    return sender.get(
        "/start"
    )

# 'result' -> 'draw' / 'position' -> '(1,1)'
def post_query(auth_key, position):
    return sender.post(
        "/query",
        {
            'auth_key': auth_key,
            'position': position
        }
    )

def position_to_string(x, y):
    return f'({x},{y})'

def string_to_position(strr):
    return int(strr[1]), int(strr[3])

dx = [[0,1,2], [0,1,2]]
dy = [[0,1,2], [2,1,0]]

def check():
    global mapp
    for i in range(3):
        count = 0
        for j in range(3):
            if mapp[i][j] == ME: count += 1
            elif mapp[i][j] == CP: count -= 1
        if count == 3: return ME
        elif count == -3: return CP

    for j in range(3):
        count = 0
        for i in range(3):
            if mapp[i][j] == ME: count += 1
            elif mapp[i][j] == CP: count -= 1
        if count == 3: return ME
        elif count == -3: return CP
    
    for q in range(2):
        count = 0
        for w in range(3):
            i, j = dx[q][w], dy[q][w]
            if mapp[i][j] == ME: count += 1
            elif mapp[i][j] == CP: count -= 1
        if count == 3: return ME
        elif count == -3: return CP

    return BLANK

def min_max(turn):
    global mapp
            
    res_score = 0
    max_score, max_x, max_y = -float('inf'), -1, -1
    for i in range(3):
        for j in range(3):
            if mapp[i][j] == BLANK:
                mapp[i][j] = turn

                check_res = check()
                if check_res == ME:
                    mapp[i][j] = BLANK
                    return 1, i, j
                elif check_res == CP:
                    mapp[i][j] = BLANK
                    return -1, i, j

                next_turn = 1 if turn == 2 else 2
                cur_res = min_max(next_turn)
                mapp[i][j] = BLANK
                res_score += cur_res[0]
                if cur_res[0] > max_score:
                    max_score = cur_res[0]
                    max_x, max_y = i, j
    
    return res_score, max_x, max_y

def get_next_position_by_map():
    res = min_max(ME)
    return res[1], res[2]

def play(auth_key, position):
    global mapp
    mapp = [[BLANK]*3 for _ in range(3)]

    if position == 'none':
        x, y = get_next_position_by_map()
        mapp[x][y] = ME
        res = post_query(auth_key, position_to_string(x, y))
        
        cx, cy = string_to_position(res['position'])
        mapp[cx][cy] = CP
    else:
        cx, cy = string_to_position(position)
        mapp[cx][cy] = CP

    while True:
        x, y = get_next_position_by_map()
        mapp[x][y] = ME
        res = post_query(auth_key, position_to_string(x, y))

        if res.get('result'):
            return res['result']
        
        cx, cy = string_to_position(res['position'])
        mapp[cx][cy] = CP


def start():
    while True:
        start_res = get_started()
        auth_key, position = start_res['auth_key'], start_res['position']
        res = play(auth_key, position)
        print(res)


if __name__ == '__main__':
    sender = RequestsSender(BASE_URL, TOKEN, CONTENT_TYPE)
    start()