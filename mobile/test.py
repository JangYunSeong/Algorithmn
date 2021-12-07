import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

db_url = 'https://teamproject-da28a-default-rtdb.firebaseio.com/'
cred = credentials.Certificate('myStockKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : db_url
})
ref = db.reference('user')
a = ref.get()
for i in a:
    url2 = "user/" + i
    url = "user/" + i + "/startStock" 
    new = db.reference(url)
    temp = new.get()
    temp[0]['stockPrice'] = 220000
    new2 = db.reference(url2)
    new2.update({'startStock' : temp})
    print(new2.get())    
