import requests
url = 'http://localhost:9000/api/encrypt'
h="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36||Lwg8gixK6qPO9kfv-ghLQQ||1536:864||win32||webkit"
h = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36||R1woA2YDPgRxNVeavW7NkQ||1536:864||win32||webkit"
data = "83,196"
res = requests.post(url,data={'data':data,"key":"338f693c945234ce1fe961b8dd844044"})

print(res.text.replace("+","-").replace("/","_").replace("=",""))


import hashlib   

m2 = hashlib.md5()   
m2.update(data.encode())   
md5data = m2.hexdigest()
print(md5data)


