from collections import defaultdict
import requests

'''
당신은 매칭을 신청한 유저들이 너무 오래 기다리지 않도록 하면서,
모든 유저가 공정하게 등급을 받을 수 있도록 매칭을 성사시켜야 한다.
'''

BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
TOKEN = "e4677bfb5512a797ba6567c21e642b01"
CONTENT_TYPE = "application/json"

class RequestsSender:
    def __init__(self, base_url, token, content_type):
        self.base_url = base_url
        self.token = token
        self.content_type = content_type
    
    def get_url(self, route):
        return BASE_URL + route if route[0] == "/" else BASE_URL + "/" + route

    def get(self, route, auth_key):
        res = requests.get(
            self.get_url(route),
            headers = {
                'Content-Type': self.content_type,
                'Authorization': auth_key
            }
        )
        return res.json()

    def post(self, route, params):
        res = requests.post(
            self.get_url(route),
            headers = {
                'Content-Type': self.content_type,
                'X-Auth-Token': self.token
            },
            params = params
        )
        return res.json()

    def put(self, route, auth_key, json):
        res = requests.put(
            self.get_url(route),
            headers = {
                'Content-Type': CONTENT_TYPE,
                'Authorization': auth_key
            },
            json = json
        )
        return res.json()
    

# { "auth_key": "1fd74321-d314-4885-b5ae-3e72126e75cc", "problem": 1, "time": 0 }
def post_start(problem):
    res = sender.post(
        "/start",
        {
            "problem": problem
        }
    )
    return res['auth_key']

# { "id": 1, "from": 3 }
def get_waiting_line(auth_key):
    res = sender.get(
        "/waiting_line",
        auth_key
    )
    #print("Waiting line", res)
    return res['waiting_line']

# { "id": 1, "grade": 2100 }
def get_user_info(auth_key):
    res = sender.get(
        "/user_info",
        auth_key
    )
    #print("User info", res)
    return res['user_info']

# { "status": "ready" }
def put_change_grade(auth_key, commands):
    res = sender.put(
        "/change_grade",
        auth_key,
        json = {
                "commands": commands
            }
    )
    #print("Change grade", res)
    return res

def get_score(auth_key):
    res = sender.get(
        "/score",
        auth_key
    )
    print("Score", res)
    return res

# { "status": "ready", "time": 312 }
def put_match(auth_key, pairs):
    res = sender.put(
        "/match",
        auth_key,
        json = {
            "pairs": pairs
        }
    )
    #print("Match", res)
    return res

# {"win": 10, "lose": 2, "taken": 7 }
def get_game_result(auth_key):
    res = sender.get(
        "/game_result",
        auth_key
    )
    #print("Game result", res)
    return res['game_result']

def get_pairs_and_change_default_grade(auth_key, waiting_line):
    commands = []
    for item in waiting_line:
        item_id, item_from = item.values()
        if not dictt.get(item_id):
            dictt[item_id] = [4000, 1]
            commands.append({ "id": item_id, "grade": 4000 })
    if len(commands) > 0:
        put_change_grade(auth_key, commands)

    waiting_line.sort(key = lambda x:x['from'])

    added = set()
    pairs = []
    for i in range(len(waiting_line)):
        i_id = waiting_line[i]["id"]
        if i_id in added: continue

        min_diff_abs = float('inf')
        min_id = 0
        for j in range(int(len(waiting_line)*0.7)):
            j_id = waiting_line[j]["id"]
            if i == j: continue
            if j_id in added: continue

            diff = abs(dictt[i_id][0] - dictt[j_id][0])
            if min_diff_abs > diff:
                min_id = j_id
                min_diff_abs = diff
        
        pairs.append([i_id, min_id])
        added.add(i_id)
        added.add(min_id)

    return pairs

def play_game():
    global dictt
    dictt = {}

    auth_key = post_start(problem = 2)
    put_match(auth_key, [])

    # 1 ~ 555: Match + Game Result + Change Grade
    # ~ 595: Game Result + Change Grade
    # 595에서 Match + Score
    for i in range(1, 596):
        print("----------", i, "---------")
        res = get_waiting_line(auth_key)
        pairs = get_pairs_and_change_default_grade(auth_key, res)
        put_match(auth_key, pairs)

        # 게임 결과를 반영
        for item in get_game_result(auth_key):
            win, lose, taken = item.values()
            if not dictt.get(win): dictt[win] = [4000, 1]
            if not dictt.get(lose): dictt[lose] = [4000, 1]

            diff = 1000
            w = (40 - taken) / 40
            next_win_grade = int((dictt[lose][0]/dictt[lose][1] + diff)*w + (dictt[win][0]/dictt[win][1])*(1-w))
            next_lost_grade = int((dictt[win][0]/dictt[win][1] - diff)*w + (dictt[lose][0]/dictt[lose][1])*(1-w))
            
            dictt[win][0] += next_win_grade
            dictt[win][1] += 1
            dictt[lose][0] += next_lost_grade
            dictt[lose][1] += 1
        #print(dictt)
    
    commands = []
    for id, data in dictt.items():
        commands.append({ "id": id, "grade": data[0]//data[1] })
    put_change_grade(auth_key, commands)
    res = get_score(auth_key)
    print(res)


if __name__ == '__main__':
    sender = RequestsSender(BASE_URL, TOKEN, CONTENT_TYPE)
    play_game()

# FIFO: 146

# 0.2 0.8 DIFF
# 'efficiency_score': '90.1067',
# 'accuracy_score1': '41.1111',
# 'accuracy_score2': '52.0786',
# 'score': '183.913'

# 0~9999 고려 + DIFF 10 + 확률
# {'status': 'finished', 'efficiency_score': '6.5515', 'accuracy_score1': '37.5556', 'accuracy_score2': '53.4188', 'score': '114.4104'}

# j_id 오류 수정, grade 4000으로 수정
# {'status': 'finished', 'efficiency_score': '99.8723', 'accuracy_score1': '31.3333', 'accuracy_score2': '51.9323', 'score': '179.8166'}