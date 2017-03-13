# -*- encoding:utf-8 -*-
import os
import time
import requests
from bs4 import BeautifulSoup

# 爬取豆瓣阅读专栏里所有专栏
num = 1
headers = {'user-agent':'Mozilla/5.0'}
for i in list(range(0,1830,10)):
	res = requests.get('https://read.douban.com/columns/category/all?sort=hot&start=%d'%i,headers=headers)
	soup = BeautifulSoup(res.text,'lxml')
	link = soup.find_all('div',class_='info') #选取爬取内容的部分
	for tushu in link:
		name = tushu.find('h4').get_text() #专栏的名字
		author = tushu.find('div',class_='author').get_text() #专栏的作者     本来也想爬取关于专栏的短简介用BeautifulSoup
		all_content = '第%d个专栏'%num+'\t' +name + '\t' + author           #    显示不完美，用一部分多余的，应该用re
		print(all_content)
		with open('F:/zhuanlan.txt','a',encoding='utf-8') as f:
			f.write(all_content+'\n')
		num = num+1
		time.sleep(1) 
		
