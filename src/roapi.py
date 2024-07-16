import requests
import time
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
authurl = 'https://auth.roblox.com/v2/logout'
baseversion = 2
updateversion = 2.0
githubversion = requests.get("https://versionsroapi.pythonanywhere.com/").json()
if githubversion["base"] != baseversion:
    print("New release found for rogamepass.py Please Download latest version at https://github.com/sesocellgames/rogamepass.py/releases/")
elif githubversion["update"] != updateversion:
    print("New update found for rogamepass.py Please Download latest version at https://github.com/sesocellgames/rogamepass.py/releases/")
class deletor:
    def __init__(self,cookie:str):
        self.cookie=cookie
    def gamepass(self,passid):
        url=f"https://www.roblox.com/game-pass/revoke"
        data={"id":passid}
        requests.post(url,data=data, headers=info.get_headers(self.cookie), cookies=info.get_cookies(self.cookie))
        print("Gamepass Deleting Done!")
class info:
    def get_user_id(cookie):
        url="https://users.roblox.com/v1/users/authenticated"
        req=requests.get(url,headers=info.get_headers(cookie),cookies=info.get_cookies(cookie))
        return req.json()['id']
    def get_info_request_url(id:int):
            return f"https://apis.roblox.com/game-passes/v1/game-passes/{id}/product-info"
    def get_info(id:int):
        url=info.get_info_request_url(id)
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
class buyer:
    def __init__(self,cookie:str):
        self.cookie=cookie
    def buy(self,delete:bool,id:int):
        info=info.get_info(id)
        data={"expectedCurrency": 1, "expectedPrice":info[2] , "expectedSellerId":info[1]}
        url1=f"https://economy.roblox.com/v1/purchases/products/{info[0]}"
        data = requests.post(url1,data=data,headers=info.get_headers(self.cookie), cookies=info.get_cookies(self.cookie))
        if delete==True:
                deletor(self.cookie).gamepass(id)
    def get_robux_amount(self):
        url=f"https://economy.roblox.com/v1/users/{info.get_user_id(self.cookie)}/currency"
        data = requests.get(url,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie))
        return data.json()["robux"]
    def auto_buy(self,id:int,amount:int,cooldown_time:int):
        for i in range(amount):
            time.sleep(cooldown_time)
            self.buy(True,id)
    def donate(self,username,amount):
        a = 0
        for passe in info.get_gamepasses(username):
            if  a+passe[1]<=amount:
                a+=passe[1]
                buyer(self.cookie).buy(True,passe[0],"pass")
        if a == amount:
            return "success"
        else:
            return f"Not found gamepass, Sended {a} Wanted {amount}"
class gamepass:
    def __init__(self,cookie:str = None):
        self.cookie=cookie
    def do_offsale(self,passid):
        url=f"https://apis.roblox.com/game-passes/v1/game-passes/{passid}/details"
        data={"IsForSale": "false"}
        a=requests.post(url,data=data,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie))
    def edit_gamepass(self,passid : int,data : list):
        url=f"https://apis.roblox.com/game-passes/v1/game-passes/{passid}/details"
        request=requests.post(url,data=data,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie))
    def check_own(self,userId,passid):
        url=f'https://inventory.roblox.com/v1/users/{userId}/items/GamePass/{passid}'
        a=requests.get(url)
        if a.json()['data']!=[]:
            return True
        return False
    def check_bought(self,passid):
         url=f"https://apis.roblox.com/game-passes/v1/game-passes/{passid}/details"
         request=requests.get(url,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie))
         if request.json()["gamePassSalesData"]["totalSales"] >= 1:
             return True
         else:
             return False
    def pass_creator(self,amount,universeid):
        url="https://apis.roblox.com/game-passes/v1/game-passes"
        data={"Name": "Gamepass Name",
        "UniverseId": universeid}
        a=requests.post(url,data=data,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie))
        try:
            passid=a.json()['gamePassId']
            url=f"https://apis.roblox.com/game-passes/v1/game-passes/{passid}/details"
            data={"IsForSale": "true","Price": amount}
            a=requests.post(url,data=data,headers=info.get_headers(self.cookie),cookies=info.get_cookies(self.cookie))
            print(a.content)
            return str(passid)
        except:
            return "Error"
