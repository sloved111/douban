# -*- encoding:utf-8 -*-
import os
import time
import requests
from bs4 import BeautifulSoup

num = 1
headers = {'user-agent':'Mozilla/5.0'}
for i in list(range(0,1830,10)):
	res = requests.get('https://read.douban.com/columns/category/all?sort=hot&start=%d'%i,headers=headers)
	soup = BeautifulSoup(res.text,'lxml')
	link = soup.find_all('h4')
	for tushu_list in link:
		title = '第%d个专栏' %num +'\t\t\t' + tushu_list.get_text()
		print(title)
		with open('F:/xiaoshuo.txt','a',encoding='utf-8') as f:
			f.write(title +'\n')
		num = num+1
		time.sleep(0.1)
		
