#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, requests

# 配置
# > 理论上可以爬取一切 Hust OJ
base_url = 'https://lydsy.com/JudgeOnline/problem.php?id={pid}'
start_id = 1000
end_id = 1010

# 创建文件夹
try:
    os.makedirs('source')
    print('Make "source" folder successfully.')
except:
    print('"source" folder has been created.')

# 从文件中获取 cookie 以爬取权限题
# 请确保你已经运行过 login.py 以获取 cookie
cookie = ''
with open('cookie.txt', 'r+') as file:
    cookie = file.read()
    file.close()

# 配置请求 Session
rq = requests.Session()
rq.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3395.99 Safari/537.36'})
rq.headers.update({'Cookie': 'PHPSESSID=%s' % cookie})

# 爬取页面

for pid in range(start_id, end_id):
    url = base_url.format(pid = pid)
    file = open('source/{pid}.html'.format(pid = pid), 'w+', encoding = 'utf8')
    ret = rq.get(url)
    ret.encoding = 'utf8'
    file.write(ret.text)
    file.close()
    print('Get problem {pid} successfully.'.format(pid = pid))
