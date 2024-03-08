import requests
import yaml
from bs4 import BeautifulSoup as bs

cred = yaml.load(open('../conf/credentials.yaml'),yaml.SafeLoader)
username= cred['wenlin']['Username']
pwd = cred['wenlin']['Password']

data = {
    "wpName": username,
    "wpPassword": pwd,
    "wploginattempt": "Log in",
    "wpEditToken": "+\ ",
    "title": "Special:UserLogin",
    "authAction": "login",
    "force": "",
}

url = 'https://wenlin.co/wanwu/index.php?title=Special:UserLogin&returnto=Main+Page'
r1 = requests.get(url)
r = requests.post(url,data,cookies=r1.cookies)


print(bs(r.content, 'html.parser').prettify())