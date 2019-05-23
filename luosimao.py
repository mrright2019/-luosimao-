import requests,re
import json,time
from random import randint
from PIL import Image
def repaire_img(path, position):
    img = Image.open(path)
    img_click = Image.new('RGB', img.size)
    for i,p in enumerate(position):
        pic = img.crop((int(p[0]), int(p[1]), int(p[0]) + 20, int(p[1]) + 80))
        box = (20 * i, 0, 20 * (i + 1), 80) if i<15 else (20 * (i - 15), 80, 20 * (i + 1 - 15), 160)
        img_click.paste(pic, box)
    img_click.save(path)

url = 'https://my.luosimao.com/auth/register'

def encrypt(data,key=None):
	url = 'http://localhost:9000/api/encrypt'
	if not  key:
		res = requests.post(url,data={'data':data})
	else:
		res = requests.post(url,data={'data':data ,"key":key})
	return json.loads(res.text)['result']


User_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {
	'User-Agent':User_agent
}

response = requests.get(url,headers=headers)
site_key = re.search('data-site-key="(.*?)"',response.text).group(0).split('"')[1]
data_id = '_hh8u5j1u7'
widget_url = 'https://captcha.luosimao.com/api/widget?k={}&l=zh-cn&s=normal&i={}'.format(site_key,data_id)
widget_response = requests.get(widget_url,headers=headers)
data_token = re.search('data-token="(.*?)"',widget_response.text).group(0).split('"')[1]
print("data_token",data_token)
_bg = "{}||{}||1536:864||win32||webkit".format(User_agent,data_token)
bg = encrypt(_bg)
begin_time = int(time.time()*1000)-1000
_b = "{},{}:{}||{},{}:{}".format(randint(180,190),randint(0,30),begin_time,randint(180,190),randint(0,30),begin_time+randint(1000,1200))
b = encrypt(_b)
requests_url = 'https://captcha.luosimao.com/api/request?k={}&l=zh-cn'.format(site_key)
# headers.update()
requests_response = requests.post(requests_url,headers=headers,data={'bg':bg,"b":b})
requests_data = json.loads(requests_response.text)
frame_url = 'https://captcha.luosimao.com/api/frame?s={}&i={}&l=zh-cn'.format(requests_data['s'],data_id)
frame_response = requests.get(frame_url,headers=headers)
res = re.search("var captchaImage = (.*?)}",frame_response.text).group(0)
res = res.replace("var captchaImage = ","").replace('p:','"p":').replace('l:','"l":').replace("'",'"')
d = json.loads(res)
imgsrc = d['p'][0]
with open('temp.jpg','wb') as f:
	print(imgsrc)
	imgcontent = requests.get(imgsrc)
	f.write(imgcontent.content)

repaire_img('temp.jpg',d['l'])
print("图片修复完成",requests_data['w'])
new_key = requests_data['i']
time.sleep(30)
da = open('pos.txt','r').read()

import hashlib  
m2 = hashlib.md5()   
m2.update(da.encode())   
parm_v = m2.hexdigest()
print(parm_v)
end_data = {
	'h':requests_data['h'],
	'v':encrypt(da,new_key).replace("+","-").replace("/","_").replace("=",""),
	's':parm_v,
}
end_res = requests.post('https://captcha.luosimao.com/api/user_verify',data = end_data,headers=headers)
print(end_res)
print(end_res.text)

