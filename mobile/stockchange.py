import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import requests
import time

db_url = 'https://teamproject-da28a-default-rtdb.firebaseio.com/'
cred = credentials.Certificate('myStockKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : db_url
})
while(1):
    now = datetime.now()
    date = str(now.year)+ "-" + str(now.month) + "-" + str(now.day)
    print(date)
    ref = db.reference('user')
    a = ref.get()
    for i in a:
        print(i)
        sum = 0
        changeUrl = "user/" + i
        changes = db.reference(changeUrl)
        changeTemp = changes.get()
        changeNum = changeTemp['changeNum']
        stockUrl = "user/" + i + "/stockChange"
        dateUrl = "user/" + i+ "/date"
        url = "user/" + i + "/currentStock"
        new = db.reference(url)
        temp = new.get()
        for i in temp:
            sum += i['stockPrice']
        if(sum == 0):
            pass
        else:
            new2 = db.reference(stockUrl)
            temp2 = new2.get()
            # new2.update({date:sum})
            new2.update({changeNum : sum})
            new3 = db.reference(dateUrl)
            new3.update({changeNum : date})
            changeNum += 1
            changes.update({'changeNum' : changeNum})
    time.sleep(3600 * 24)
