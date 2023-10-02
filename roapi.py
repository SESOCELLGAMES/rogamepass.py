import requests
import time
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
authurl = 'https://auth.roblox.com/v2/logout'
#authurl is to get xsrf token that doesn't logout of your account
print("Made by Okis Modified by Sesocell")
class deleter:
    def __init__(self,cookie:str):
        self.cookie=cookie
    def delete_asset(self,assetid):
        url=f"https://www.roblox.com/asset/delete-from-inventory"
        data={"assetId":assetid}
        requests.post(url,data=data, headers=info.get_headers(self.cookie), cookies=info.get_cookies(self.cookie))
        print("Item Is Deleted")
    def delete_pass(self,passid):
        url=f"https://www.roblox.com/game-pass/revoke"
        data={"id":passid}
        requests.post(url,data=data, headers=info.get_headers(self.cookie), cookies=info.get_cookies(self.cookie))
        print("Gamepass Is Deleted")
class info:
    def get_user_id(cookie):
        url="https://users.roblox.com/v1/users/authenticated"
        req=requests.get(url,headers=info.get_headers(cookie),cookies=info.get_cookies(cookie))
        return req.json()['id']
    def get_info_request_url(type:str,id:int):
        if type=="gamepass":
            return f"https://apis.roblox.com/game-passes/v1/game-passes/{id}/product-info"
        elif type=="asset":
            return f"https://economy.roblox.com/v2/assets/{id}/details"
    def get_info(id:int,type:str):
        url=info.get_info_request_url(type,id)
        req=requests.get(url)
        list=[]
        list.append(req.json()['ProductId'])
        list.append(req.json()['Creator']['Id'])
        list.append(req.json()['PriceInRobux'])
        return list
    def getXsrf(cookie):
        xsrfRequest = requests.post(authurl, headers={'User-Agent': useragent}, cookies=info.get_cookies(cookie))
        if xsrfRequest.headers['x-csrf-token']:
            return xsrfRequest.headers['x-csrf-token']
        else:
            return ''
    def get_headers(cookie):
        return {"X-CSRF-TOKEN":info.getXsrf(cookie)}
    def get_cookies(cookie):
        return {".ROBLOSECURITY":cookie}
    def getUserId(username):
        API_ENDPOINT = "https://users.roblox.com/v1/usernames/users"
        payload={'usernames':[username],}
        req=requests.post(API_ENDPOINT,json=payload)
        return req.json()['data'][0]['id']
    def get_gamepasses(username):
        url=f"https://games.roblox.com/v2/users/{info.getUserId(username)}/games?accessFilter=Public&limit=50"
        req=requests.get(url)
        ids=[]
        for game in req.json()['data']:
            ids.append(game['id'])
        gamepasses=[]
        for universe in ids:
            url=f'https://games.roblox.com/v1/games/{universe}/game-passes?limit=100&sortOrder=Asc'
            otherequest=requests.get(url)
            for gamepass in otherequest.json()['data']:
                a=[]
                if not gamepass['price']==None:
                    a.append(gamepass['id'])
                    a.append(gamepass['price'])
                    gamepasses.append(a)
        return gamepasses
class Buyer:
    def __init__(self,cookie:str):
        self.cookie=cookie
    def buy(self,delete:bool,id:int,type:str):
        info=info.get_info(id,type)
        data={"expectedCurrency": 1, "expectedPrice":info[2] , "expectedSellerId":info[1]}
        url1=f"https://economy.roblox.com/v1/purchases/products/{info[0]}"
        data = requests.post(url1,data=data,headers=info.get_headers(self.cookie), cookies=info.get_cookies(self.cookie))
        print(data.content)
        if delete==True:
            if type=="gamepass":
                deleter(self.cookie).delete_pass(id)
            elif type=="asset":
                deleter(self.cookie).delete_asset(id)
    def get_robux_amount(self):
        url=f"https://economy.roblox.com/v1/users/{info.get_user_id(self.cookie)}/currency"
        data = requests.get(url,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie) )
        print(data.json())
        return data.json()["robux"]
    def auto_buy(self,id:int,type:str,amount:int,cooldown_time:int):
        for i in range(amount):
            time.sleep(cooldown_time)
            self.buy(True,id,type)
    def donate(self,username,amount):
        a=0
        for passe in info.get_gamepasses(username):
            if  a+passe[1]<=amount:
                a+=passe[1]
                Buyer(self.cookie).buy(True,passe[0],"pass")
        if a==amount:
            return "success"
        else:
            return f"Not found gamepass ,Sended {a} Wanted {amount}"
