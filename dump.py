#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, re, json

# 配置
start_id = 1000
end_id = 1010

# 创建文件夹
try:
    os.makedirs('json')
    print('Make "json" folder successfully.')
except:
    print('"json" folder has been created.')

# 转换为 json
for pid in range(start_id, end_id):
    rfile = open('source/{pid}.html'.format(pid = pid), 'r+', encoding = 'utf8')
    wfile = open('json/{pid}.json'.format(pid = pid), 'w+', encoding = 'utf8')
    html = rfile.read()
    title = re.search(r'<title[\s\S]*?title>', html).group()[24:-8]
    content = re.search(r'<h2>Description</h2>[\s\S]*?<center>', html).group()[:-8]
    data = {'id': pid, 'title': title, 'content': content}
    wfile.write(json.dumps(data, ensure_ascii = False))
    rfile.close()
    wfile.close()
    print('Dump problem {pid} successfully.'.format(pid = pid))
