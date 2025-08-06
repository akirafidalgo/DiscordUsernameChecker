import requests
import json
DISCORD_TOKEN = input("discord token: ")

HEADERS = {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": DISCORD_TOKEN,
    "content-type": "application/json",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}

API_URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"

def check_username(username):
    data = {
        "username": username
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        res = response.json()
        taken = res.get("taken", None)
        if taken is not None:
            print(f"username '{username}' taken: {taken}")
        else:
            print(f"unexpected response.")
    elif response.status_code == 401:
        print("invalid token.")
    elif response.status_code == 429:
        print("[⏳] Rate limited. Try again in a bit.")
    else:
        try:
            print(f"fail: {response.status_code} - {response.json()}")
        except:
            print(f"fail: {response.status_code} - {response.text}")


while True:
    username = input("\nEnter username to check (or type 'exit'): ").strip()
    if username.lower() == "exit":
        break
    check_username(username)
