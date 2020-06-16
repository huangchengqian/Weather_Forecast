import requests
from urllib import parse
import json

'''
	关于api
	包含账号信息 appi、appsecret
	后面包含可选参数 参见：https://tianqiapi.com/index/doc
'''


def getInfo(cityId):
	u = 'https://tianqiapi.com/api?version=v6&appid=11853423&appsecret=SC3aTUDe&cityid='
	# url = parse.urljoin(u, city)
	url = u + cityId
	# print(url)
	respon = requests.get(url)
	w_text = respon.text
	return w_text
