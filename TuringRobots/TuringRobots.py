# -*- coding: utf-8 -*-
# @Time    : 2022/6/18 11:34
# @Author  : AI悦创
# @FileName: TuringRobots.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import json
import urllib.request
import os
# from dotenv import load_dotenv


def TuringRobots(text, over_print=True):
	"""
	:param text:
	:param over_print:
	:return:
	"""
	# load_dotenv()
	api_url = "http://openapi.tuling123.com/openapi/api/v2"
	req = {
		"reqType": 0,
		"perception":
			{
				"inputText":
					{
						"text": text
					},
				"selfInfo":
					{
						"location":
							{
								"city": "厦门",
								"province": "厦门",
								"street": "海沧区"
							}
					}
			},
		"userInfo":
			{
				"apiKey": "27f4569b10c84a73aadb819b3b3598b0",
				# "apiKey": os.getenv("API_KEY"),
				"userId": "OnlyUseAlphabet"
			}
	}
	# print(req)
	# 将字典格式的req编码为utf8
	req = json.dumps(req).encode('utf8')
	# print(req)

	http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
	response = urllib.request.urlopen(http_post)
	response_str = response.read().decode('utf8')
	# print(response_str)
	response_dic = json.loads(response_str)
	# print(response_dic)

	intent_code = response_dic['intent']['code']
	results_text = response_dic['results'][0]['values']['text']
	if over_print:
		print('Turing的回答：')
		print('code：' + str(intent_code))
		print('text：' + results_text)
		return None
	else:
		return (str(intent_code), results_text)


if __name__ == '__main__':
	text = input("请输入你的对话：")
	code, content = TuringRobots(text, over_print=False)
	print(code, content)
