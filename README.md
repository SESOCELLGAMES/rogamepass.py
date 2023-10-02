# ROAPI
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
