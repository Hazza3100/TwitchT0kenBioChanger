import requests
import random
import threading

from colorama import Fore, init

init(convert=True)


bio = input("Enter New Bio for tokens: ")


def ChangeBio():

    url = 'https://id.twitch.tv/oauth2/validate'

    tokenf = open("tokens.txt")
    token = random.choice(tokenf.read().splitlines())
    tokenf.close()

    headers = {
        "Authorization": "Bearer " + token
    }
    r = requests.get(url, headers=headers)
    user_id = r.json()['user_id']
    username = r.json()['login']
    requests.post(url, headers=headers)

    headers = {"Connection": "keep-alive","Pragma": "no-cache","Cache-Control": "no-cache","sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',"Accept-Language": "pl-PL","sec-ch-ua-mobile": "?0","Client-Version": "e8881750-cfb7-4ff7-aaae-132abb1e8259","Authorization": f"OAuth {token}","Content-Type": "text/plain;charset=UTF-8","User-agent": f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',"Client-Session-Id": "671362f9f83b6729","Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko","X-Device-Id": "O1MrFLwPyZ2byJzoLFT0K5XNlORNRQ9F","sec-ch-ua-platform": '"Windows"',"Accept": "*/*","Origin": "https://dashboard.twitch.tv","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://dashboard.twitch.tv/",}
    json = [{"operationName": "UpdateUserProfile","variables": {"input": {"displayName": username,"description": bio,"userID": user_id,}},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "991718a69ef28e681c33f7e1b26cf4a33a2a100d0c7cf26fbff4e2c0a26d15f2",}},}]
    r = requests.post("https://gql.twitch.tv/gql",headers=headers, json=json)
    print(Fore.GREEN + f"[+]{Fore.RESET} Updated {token}\n")



def start():
    print("Hazey Changer\ndiscord.gg/KAgSf3pwjE")
    amount = open('tokens.txt', 'r').read
    for x in amount():
        x = threading.Thread(target=ChangeBio)
        x.start()


start()
