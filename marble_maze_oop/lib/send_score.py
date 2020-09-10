import requests


def create_post(player_name, level, tries, score):
    payload = {"Player_name": player_name, "level": level, "try": tries, "score": score}
    r = requests.post('http://167.172.37.168/api/newscore', data=payload)
    print(r.text)
    print(r.status_code)

