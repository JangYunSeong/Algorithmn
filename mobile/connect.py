import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time

def get_code(company_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_code(company_code)
    no_today = bs_obj.find("p", {"class" : "no_today"})
    if(no_today == None):
        return "0"
    else:
        blind = no_today.find("span", {"class" : "blind"})
        now_price = blind.text
        return now_price

def strToInt(str):
    index = 1
    result = 0
    for i in range(len(str)-1, -1,-1):
        if(str[i] == ','):
            pass
        else:
            result += int(str[i]) * index
            index *= 10
    return result
# def get_name(company_code):
#     bs_obj = get_code(company_code)
#     com_name = bs_obj.find("h2", {"class" : "wrap_company"})
#     company_name = com_name.text
#     return company_name

db_url = 'https://teamproject-da28a-default-rtdb.firebaseio.com/'
cred = credentials.Certificate('myStockKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : db_url
})
while(1):
    now = datetime.now()
    print(now)
    ref = db.reference('user')
    a = ref.get()
    for i in a:
        print(i)
        stockUrl = "user/" + i
        url = "user/" + i + "/startStock" 
        new = db.reference(url)
        temp = new.get()
        for i in temp:
            now_price = strToInt(get_price(i['stockCode']))
            i['stockPrice'] = i['stockNum'] * now_price
            print(i['stockName'] +' : ' ,now_price)
        new2 = db.reference(stockUrl)
        new2.update({'currentStock' : temp})
    time.sleep(60)