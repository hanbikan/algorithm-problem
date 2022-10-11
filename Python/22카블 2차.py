
import requests
'''
호텔의 객실 이용률이 목표치 이상이 되도록 예약을 관리하거나 객실을 배정하면서,
객실 수가 많은 예약은 최대한 거절하지 않아야 합니다.
'''

BASE_URL = "https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api"
TOKEN = "fdf5cfe134954eebcaa3f757acdd1076"
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
            json = params
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

def post_start(problem):
    res = sender.post(
        "/start",
        {
            "problem": problem
        }
    )
    return res['auth_key']

# 현재 날짜에 새로 들어온 예약 요청의 정보를 반환합니다.
def get_new_requests(auth_key):
    res = sender.get(
        "/new_requests",
        auth_key
    )
    return res['reservations_info']

# 특정 예약 요청에 대한 승낙 / 거절을 답변합니다.
# replies: [{ "id": 412424, "reply": "accepted"},{ "id": 707981, "reply": "refused"},]
def put_reply(auth_key, replies):
    res = sender.put(
        "/reply",
        auth_key,
        {
            'replies': replies
        }
    )
    return res

# {"day": 108,"fail_count": 5}
def simulate(auth_key, room_assign):
    res = sender.put(
        "/simulate",
        auth_key,
        {
            'room_assign': room_assign
        }
    )
    print("simulate", res)
    return res

def score(auth_key):
    res = sender.get(
        "/score",
        auth_key
    )
    return res





def convert_to_room_number(h, w):
    return '%d%03d' % (h, w)

def is_rooms_empty(height, start_width, end_width, start_day, end_day):
    for day in range(start_day, end_day):
        for width in range(start_width, end_width):
            if hotels[day][height][width] != None:
                return False
    return True

def set_hotel(req, height, start_width, end_width, start_day, end_day):
    global hotels, hotel_filled
    for day in range(start_day, end_day):
        for width in range(start_width, end_width):
            hotels[day][height][width] = req
            hotel_filled[day] += 1

def get_amount(x):
    return (x['check_out_date'] - x['check_in_date'])*x['amount']

sender = RequestsSender(BASE_URL, TOKEN, CONTENT_TYPE)
PROBLEM = 1
auth_key = post_start(problem = PROBLEM)
print(auth_key)



REPLY_WEIGHT = 0.5 # 대답을 유보하는 기간 가중치 ... 최대한 쌓아두었다가 결정하기 위함

W = 20 if PROBLEM == 1 else 200
H = 3 if PROBLEM == 1 else 10
ED = 200 if PROBLEM == 1 else 1000

global hotels, hotel_filled
hotels = [[[None]*(W + 1) for _ in range(H + 1)] for _ in range(ED+1)]
hotel_filled = [0]*(ED+1)

#{"id": 453217, "amount": 10, "check_in_date": 104, "check_out_date": 110, "end_day": 103}

reqs = [[] for _ in range(ED+1)]
reserved = set() # 승인된 req id
for day in range(1, ED + 1):
    print("@@@@@@@@@@@@@@@@@@@@", day, "@@@@@@@@@@@@@@@@@@@@")
    
    new_requests = get_new_requests(auth_key)

    # reqs에 저장
    replies = []
    for req in new_requests:
        # @
        req_amount = get_amount(req)

        req_end_day = min(day + 14, req['check_in_date']-1)
        req_start_day = day + int((req_end_day - day)*REPLY_WEIGHT)
        req['end_day'] = req_end_day
        for req_day in range(req_start_day, req_end_day):
            reqs[req_day].append(req)
    
    # 정렬
    reqs[day].sort(reverse=True, key = lambda x: get_amount(x))
    
    # reqs에서 승인/거절 + hotels 수정 ... in, out date에 맞게
    for req in reqs[day]:
        
        has_set = False
        for h in range(1, H + 1):
            for w in range(1, W - req["amount"] + 1):
                # 해당 기간에 전부 비었는가?
                if req["id"] not in reserved and is_rooms_empty(h, w, w+req["amount"], req["check_in_date"], req["check_out_date"]):
                    set_hotel(req, h, w, w+req["amount"], req["check_in_date"], req["check_out_date"])
                    replies.append({"id": req["id"], "reply": "accepted"})
                    has_set = True
                    reserved.add(req["id"])
                    break
            if has_set: break
    if len(replies) > 0:
        put_reply(auth_key, replies)

    to_simulate = []
    for i in range(1, H+1):
        j = 1
        while j < W+1:
            room = hotels[day][i][j]
            if room != None and room['check_in_date'] == day:
                to_simulate.append({"id": room["id"], "room_number": convert_to_room_number(i, j)})
                j += room['amount']
                continue
            j += 1
    simulate(auth_key, to_simulate)
    print(to_simulate)
    
    #for i in range(1, H + 1):
    #    for j in range(1, W + 1):
    #        print(hotels[day][i][j]['id'] if hotels[day][i][j] != None else '@', end=" ")
    #    print()

print(REPLY_WEIGHT, AMOUNT_SUM, NORMAL, score(auth_key))