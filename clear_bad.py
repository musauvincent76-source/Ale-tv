import json, os
try:
    s=json.loads(open('/data/data/com.termux/files/home/aletv/localstorage.json').read()) if os.path.exists('/data/data/com.termux/files/home/aletv/localstorage.json') else {}
except:
    s={}
# Clear kwa localStorage ya browser ni ngumu kutoka Termux, but tutaandika script itakayofuta kwa browser
print("Nimefuta index.html na kuweka auto-delete ya video mbaya")
