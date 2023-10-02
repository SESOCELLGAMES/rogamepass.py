# ROAPI

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

Gamepass apis for roblox 

# Example Usage
```py
import requests
from roapi import bilgi
cookie="PUT_YOUR_COOKIE"
class game_pass:
    def __init__(self,cookie:str):
        self.cookie=cookie
    def do_offsale(self,passid):
        url=f"https://apis.roblox.com/game-passes/v1/game-passes/{passid}/details"
        data={"IsForSale": "false"}
        a=requests.post(url,data=data,headers=bilgi.get_headers(self.cookie),cookies=bilgi.get_cookies(self.cookie))
    def pass_creator(self,amount,universeid):
        url="https://apis.roblox.com/game-passes/v1/game-passes"
        data={"Name": "Gamepass Name",
        "UniverseId": universeid}
        a=requests.post(url,data=data,headers=bilgi.get_headers(self.cookie),cookies=bilgi.get_cookies(self.cookie))
        try:
            passid=a.json()['gamePassId']
            url=f"https://apis.roblox.com/game-passes/v1/game-passes/{passid}/details"
            data={"IsForSale": "true","Price": amount}
            a=requests.post(url,data=data,headers=bilgi.get_headers(self.cookie),cookies=bilgi.get_cookies(self.cookie))
            print(a.content)
            return str(passid)
        except:
            return "Error"
game_pass(cookie).pass_creator(amount,universeid)

```

[contributors-shield]: https://img.shields.io/github/contributors/sesocell/roapi.svg?style=for-the-badge
[contributors-url]: https://github.com/sesocell/roapi/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sesocell/roapi.svg?style=for-the-badge
[forks-url]: https://github.com/sesocell/roapi/network/members
[stars-shield]: https://img.shields.io/github/stars/sesocell/roapi.svg?style=for-the-badge
[stars-url]: https://github.com/sesocell/roapi/stargazers
[issues-shield]: https://img.shields.io/github/issues/sesocell/roapi.svg?style=for-the-badge
[issues-url]: https://github.com/sesocell/roapi/issues
