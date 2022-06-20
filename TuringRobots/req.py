# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 23:51
# @Author  : AI悦创
# @FileName: req.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import urllib.request
def req():
	response = urllib.request.urlopen('https://bornforthis.cn/TuringRobots.html')
	html = response.read().decode("utf-8")
	# print(type(html))
	return html